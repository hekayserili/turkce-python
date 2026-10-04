# tpy/matematik.py
import math

pi = math.pi
e_sayısı = math.e

def karekök(x):
    return math.sqrt(x)

def üs(x, y):
    return math.pow(x, y)

def mutlak(x):
    return math.fabs(x)

def taban(x):
    return math.floor(x)

def tavan(x):
    return math.ceil(x)

def faktöriyel(x):
    return math.factorial(x)

def ebob(x, y):
    return math.gcd(x, y)

def ekok(x, y):
    return math.lcm(x, y)