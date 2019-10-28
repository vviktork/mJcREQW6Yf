import base64
from .models import Common
from .rest_api import rest_api
from django.core.files.base import ContentFile


def th_refresh(data):
    for obj in data.all().values():
        graf = Common.objects.get(id=obj['id'])
        data_s = rest_api('servis2', [str(graf.formula), graf.interval, graf.dt])
        if type(data_s['data']) is not str:
            data_s = rest_api('servis3', data_s)
            data_b = base64.b64decode(data_s['data'])
            graf.images.save('image.png', ContentFile(data_b))
            graf.save()
        else:
            graf.save()