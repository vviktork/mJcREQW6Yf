# -*- coding: utf-8 -*-

import base64
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .rest_api import rest_api
from .models import Functions, Common
from .th_refresh import th_refresh
from django.core.files.base import ContentFile
from .tasks import th_refresh


admin.site.site_url = None
admin.site.site_header = 'Панель Администратора'
admin.site.index_title = None
admin.site.disable_action('delete_selected')
admin.site.unregister(Group)


@admin.register(Common)
class CommonAdmin(admin.ModelAdmin):
    list_display = ('formula', 'image_img', 'interval', 'dt', 'time')
    readonly_fields = ['image_img',]
    fields = ('formula', 'interval', 'dt')
    actions = ['check_active']

    def check_active(self, request, queryset):
        id_queryset = [obj['id'] for obj in queryset.all().values()]
        th_refresh.delay(id_queryset)

    check_active.short_description = "Обновить"

    def response_change(self, request, obj):
        result = super(CommonAdmin, self).response_change(request, obj)
        data_s = rest_api('servis2', [str(obj), obj.interval, obj.dt])
        if type(data_s['data']) is not str:
            data_s = rest_api('servis3', data_s)
            data_b = base64.b64decode(data_s['data'])
            obj.images.save('image.png', ContentFile(data_b))
            obj.save()
        return result

    def response_add(self, request, obj, post_url_continue=None):
        result = super(CommonAdmin, self).response_add(request, obj, post_url_continue)
        obj.save()
        data_s = rest_api('servis2', [str(obj), obj.interval, obj.dt])
        if type(data_s['data']) is not str:
            data_s = rest_api('servis3', data_s)
            data_b = base64.b64decode(data_s['data'])
            obj.images.save('image.png', ContentFile(data_b))
            obj.save()
        return result


@admin.register(Functions)
class FunctionsAdmin(admin.ModelAdmin):
    list_display = ('formula',)
    fields = ('formula',)
    actions = None