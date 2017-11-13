from __future__ import division
from fractions import gcd

def add_frac(frac1, frac2):
    if frac1[1] != 0 and frac2[1] != 0: 
        l = frac1[0]*frac2[1] + frac2[0]*frac1[1]
        m = frac1[1] * frac2[1]
        g = gcd(l,m)
        return [l/g, m/g]
    else:
        return False

def sub_frac(frac1, frac2):
    if frac1[1] != 0 and frac2[1] != 0: 
        l = frac1[0]*frac2[1] - frac2[0]*frac1[1]
        m = frac1[1] * frac2[1]
        g = gcd(l,m)
        return [l/g, m/g]
    else:
        return False

def mul_frac(frac1, frac2):
    if frac1[1] != 0 and frac2[1] != 0: 
        l = frac1[0] * frac2[0]
        m = frac1[1] * frac2[1]
        g = gcd(l,m)
        return [l/g, m/g]
    else:
        return False

def div_frac(frac1, frac2):
    if frac1[1] != 0 and frac2[1] and frac2[0] != 0:
        return mul_frac(frac1,[frac2[1],frac2[0]])
    else:
        return False

def is_positive(frac):
    if frac[0] > 0 and frac[1] >0:
        return True
    else:
        return False

def is_zero(frac):
    if frac[0] == 0 and frac[1] != 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    sub = frac2float(sub_frac(frac1,frac2))
    if sub > 0:
        return 1
    elif sub == 0:
        return 0
    elif sub < 0:
        return -1
    else:
        return sub

def frac2float(frac):
    if frac[1] != 0:
        return frac[0]/frac[1]
    else:
        return False