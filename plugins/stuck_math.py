# -*- coding: utf-8 -*-

import math
import itertools

NAME    = 'Stuck Math'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Basic math functions plugin for the Stuck programming language.'

def add_(s): return s + [s.pop(-2)+s.pop()]
def sub_(s): return s + [s.pop(-2)-s.pop()]
def mul_(s): return s + [s.pop(-2)*s.pop()]
def mod_(s): return s + [s.pop(-2)%s.pop()]
def gth_(s): return s + [s.pop(-2)>s.pop()]
def lth_(s): return s + [s.pop(-2)<s.pop()]
def eql_(s): return s + [s.pop(-2)==s.pop()]
def bsl_(s): return s + [float(int(s.pop(-2))<<int(s.pop()))]
def bsr_(s): return s + [float(int(s.pop(-2))>>int(s.pop()))]
def sqr_(s): return s + [s.pop()**2]
def sqt_(s): return s + [s.pop()**0.5]
def fac_(s): return s + [math.factorial(s.pop())]
def spi_(s): return s + [math.pi]
def eee_(s): return s + [math.e]
def abs_(s): return s + [abs(s.pop())]
def cil_(s): return s + [math.ceil(s.pop())]
def flr_(s): return s + [math.floor(s.pop())]
def div_(s):
    return s + [(0.0+s.pop(-2))/(0.0+s.pop())]
def pwr_(s):
    n,x = s.pop(-2),s.pop()
    if int(n)==n and int(x)==x:
        return s + [int(n)**int(x)]
    else:
        try: return s + [n**x]
        except: return s + [int(n)**int(x)]
def len_(s):
    if type(s[-1]) is list and len(s[-1]) == 4:
        k = s.pop()
        return s + [((k[0]-k[2])**2+(k[1]-k[3])**2)**0.5]
    elif type(s[-1]) is list and len(s[-1]) == 2:
        k = s.pop()
        return s + [(k[0]**2+k[1]**2)**0.5]
    else:
        return s + [((s.pop(-4)-s.pop(-2))**2+(s.pop(-2)-s.pop())**2)**0.5]
def sum_(s):
    k = 0.0
    if type(s[-1]) is list:
        k = sum(s.pop())
    else:
        while s: k += s.pop()
    return s + [k]
def rmp_(s):
    k = 1.0
    if type(s[-1]) is list:
        k = reduce(lambda x,y: x*y, s.pop(), 1)
    else:
        while s: k *= s.pop()
    return s + [k]
def ctp_(s):
    k = s.pop()
    if type(k) is int or (type(k) is float and int(k) == k):
        ls = []
        while k:
            ls = [s.pop()] + ls
            k -= 1
        return s + [list(itertools.product(*ls))]
    else:
        r = s.pop()
        return s + [list(itertools.product(r,k))]
def prm_(s):
    k = s.pop()
    n = s.pop()
    return s + [math.factorial(n)/math.factorial(n-k)]
def cmb_(s):
    k = s.pop()
    n = s.pop()
    return s + [math.factorial(n)/(math.factorial(k)*(math.factorial(n-k)))]
def pri_(s):
    def expand(n):
        c = 1
        for i in xrange(int(n**.5)+1):
            c = c*(n-i)/(i+1)
            yield c
    v = s.pop()
    if v == 2:
        return s + [True]
    if v <= 1:
        return s + [False]
    for k in expand(v):
        if k%v:
            return s + [False]
    return s + [True]
        

CMDS = { '+' : add_, '-' : sub_, '*' : mul_,
         '/' : div_, '%' : mod_, '^' : pwr_,
         '#' : sqr_, '\\': sqt_, '>' : gth_,
         '<' : lth_, '=' : eql_, '{' : bsl_,
         '}' : bsr_, '`' : len_, u'Σ': sum_,
         u'Π': rmp_, '!' : fac_, u'π': spi_,
         '|' : abs_, 'X' : ctp_, 'e' : eee_,
         '(' : cil_, ')' : flr_, 'P' : prm_,
         'M' : cmb_, 'v' : pri_ }
