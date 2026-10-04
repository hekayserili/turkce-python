# tpy/rastgele.py
import random

def rastgele_sayı(alt, üst):
    return random.randint(alt, üst)

def seç(liste):
    return random.choice(liste)

def karıştır(liste):
    return random.shuffle(liste)

def rastgele():
    return random.random()

def örneklem(liste, k):
    return random.sample(liste, k)