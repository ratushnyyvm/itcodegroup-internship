from lesson_3.task_1 import get_date_and_weather
import pytest


@pytest.mark.parametrize(
    "data, month, temp, expected",
    [
        ('1', 'январь', -6, 'Cегодня 1 января. На улице -6 градусов.\nХолодно, лучше остаться дома.'),
        ('2', 'февраль', -5, 'Cегодня 2 февраля. На улице -5 градусов.\nХолодно, лучше остаться дома.'),
        ('3', 'март', -4, 'Cегодня 3 марта. На улице -4 градусов.\nХолодно, лучше остаться дома.'),
        ('4', 'апрель', -3, 'Cегодня 4 апреля. На улице -3 градусов.\nХолодно, лучше остаться дома.'),
        ('5', 'май', -2, 'Cегодня 5 мая. На улице -2 градусов.\nХолодно, лучше остаться дома.'),
        ('6', 'июнь', -1, 'Cегодня 6 июня. На улице -1 градусов.\nХолодно, лучше остаться дома.'),
        ('7', 'июль', 0, 'Cегодня 7 июля. На улице 0 градусов.'),
        ('8', 'август', 1, 'Cегодня 8 августа. На улице 1 градусов.'),
        ('9', 'сентябрь', 2, 'Cегодня 9 сентября. На улице 2 градусов.'),
        ('10', 'октябрь', 3, 'Cегодня 10 октября. На улице 3 градусов.'),
        ('11', 'ноябрь', 4, 'Cегодня 11 ноября. На улице 4 градусов.'),
        ('12', 'декабрь', 5, 'Cегодня 12 декабря. На улице 5 градусов.'),
    ]
)
def test_get_date_and_weather(data, month, temp, expected):
    msg = get_date_and_weather(data, month, temp)
    assert msg == expected
