# https://stackoverflow.com/a/43690506/11110014

import random
import string
import requests

from time import time

def human_size(size, decimal_places=2):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024.0 or unit == 'PiB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def gen_uuid(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


# print (gen_uuid(10, "AEIOSUUGTUGFMA23"))

def getspeed(start_time, downloaded_bytes):
    # get time in milisec
    total_ms = (time() - start_time) * 1000
    #in bytes
    total_bytes = downloaded_bytes * 8000
    return pretty_speed((total_bytes / total_ms)/8)


def pretty_speed(speed):
    units = ['Bps', 'KBps', 'MBps', 'GBps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.2f %s' % (speed, units[unit])

# Eta = size - downloaded bytes / speed


def get_readable_time(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result

def UserAgent():
    try:
        res = requests.get('https://fake-useragent.herokuapp.com/browsers/0.1.11').json()['browsers']
        browser = random.choice(list(res.values()))
        user_agent_list = random.choice(res[browser])
    except KeyError:
        user_agent_list = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    return user_agent_list