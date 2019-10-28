# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from Alyticstest.celery import app
from celery import shared_task
from django.core.files.base import ContentFile
import time
import numpy as np
from io import BytesIO
from matplotlib import pyplot as plt
from .models import Common


@shared_task
def th_refresh(data):

    def dot_graf(data):
        hour = 3600
        day = 24
        time_now = int(int(time.time()) / hour) * hour
        time_int = int(((time_now - data[1] * hour * day) / hour)) * hour
        time_dt = int((time_now - time_int) / (data[2] * hour))
        if time_dt == 0:
            return 'Высокий шаг для данного интервала'
        x_data = np.linspace(time_now, time_int, time_dt, dtype='int32')
        y = []
        if data[0] == 'sin(t)':
            y += (np.sin(time_now - i) for i in x_data)
        elif data[0] == 't + 2/t':
            for i in x_data:
                if time_now == i:
                    y += [float(time_now - i)]
                else:
                    y += [(time_now - i) + 2 / (time_now - i)]
        else:
            return 'Функция не существует'
        x = []
        for i in x_data: x += [time.strftime('%d/%m %H:%M', time.localtime(i))]
        return [x, y]

    def image_graph(data):
        plt.figure(figsize=(10, 10))
        plt.plot(data[0], data[1], color='orange', )
        plt.scatter(data[0], data[1], color='orange', )
        if len(data[0]) > 8: plt.xticks(rotation=60)
        plt.grid(axis='y')
        image = BytesIO()
        plt.savefig(image, format="PNG", block=False)
        images = image.getvalue()
        return images

    for obj in data:
        graf = Common.objects.get(id=obj)
        data_s = dot_graf([str(graf.formula), graf.interval, graf.dt])
        if type(data_s) is not str:
            data_s2 = image_graph(data_s)
            # Настроить отображение графиков, celery не сохраняет изображение в каталог. Снять # для теста
            #graf.images.save('image.png', ContentFile(data_s2))
            graf.save()
        else:
            graf.save()