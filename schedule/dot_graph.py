import numpy as np
import time


def dot_graf(data):
    hour = 3600
    day = 24
    time_now = int(int(time.time()) / hour) * hour
    time_int = int(((time_now - data['interval'] * hour * day) / hour)) * hour
    time_dt = int((time_now - time_int) / (data['dt'] * hour))
    if time_dt == 0:
        return 'Высокий шаг для данного интервала'
    x_data = np.linspace(time_now, time_int, time_dt, dtype='int32')
    y = []
    if data['formula'] == 'sin(t)':
        y += (np.sin(time_now - i) for i in x_data)
    elif data['formula'] == 't + 2/t':
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