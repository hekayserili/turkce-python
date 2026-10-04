# tpy/zaman.py
import time

def bekle(saniye):
    time.sleep(saniye)

def zaman():
    return time.time()

def yerel_zaman():
    return time.ctime()