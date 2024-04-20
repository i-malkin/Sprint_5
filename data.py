import random


class BurgersTestData:
    AUTH_NAME = 'Malkin_7'
    AUTH_EMAIL = 'malkin@yandex.ru'
    AUTH_PASSWORD = 'qwerty'
    AUTH_RANDOM_EMAIL = f'Malkin_7{random.randint(100, 999)}@yandex.ru'
    AUTH_PASSWORD_NEGATIVE = '1234'