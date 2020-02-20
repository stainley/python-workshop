from datetime import datetime


def get_the_time():
    return datetime.now()


print(get_the_time())


def add_suffix(suffix='.com'):
    return 'google' + suffix


def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

