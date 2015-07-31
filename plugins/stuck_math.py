# -*- coding: utf-8 -*-

import math

NAME    = 'Stuck Math'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Basic math functions plugin for the Stuck programming language.'

def add_(s): s += [s.pop(-2)+s.pop()]
def sub_(s): s += [s.pop(-2)-s.pop()]
def mul_(s): s += [s.pop(-2)*s.pop()]
def mod_(s): s += [s.pop(-2)%s.pop()]
def gth_(s): s += [s.pop(-2)>s.pop()]
def lth_(s): s += [s.pop(-2)<s.pop()]
def eql_(s): s += [s.pop(-2)==s.pop()]
def bsl_(s): s += [float(int(s.pop(-2))<<int(s.pop()))]
def bsr_(s): s += [float(int(s.pop(-2))>>int(s.pop()))]
def sqr_(s): s += [s.pop()**2]
def sqt_(s): s += [s.pop()**0.5]
def fac_(s): s += [math.factorial(s.pop())]
def spi_(s): s += [math.pi]
def div_(s):
    s += [(0.0+s.pop(-2))/(0.0+s.pop())]
def pwr_(s):
    n,x = s.pop(-2),s.pop()
    if int(n)==n and int(x)==x:
        s += [int(n)**int(x)]
    else:
        try: s += [n**x]
        except: s += [int(n)**int(x)]
def len_(s):
    if type(s[-1]) is list and len(s[-1]) == 4:
        k = s.pop()
        s += [((k[0]-k[2])**2+(k[1]-k[3])**2)**0.5]
    elif type(s[-1]) is list and len(s[-1]) == 2:
        k = s.pop()
        s += [(k[0]**2+k[1]**2)**0.5]
    else:
        s += [((s.pop(-4)-s.pop(-2))**2+(s.pop(-2)-s.pop())**2)**0.5]
def sum_(s):
    k = 0.0
    if type(s[-1]) is list:
        k = sum(s.pop())
    else:
        while s: k += s.pop()
    s += [k]
def rmp_(s):
    k = 1.0
    if type(s[-1]) is list:
        k = reduce(lambda x,y: x*y, s.pop(), 1)
    else:
        while s: k *= s.pop()
    s += [k]

CMDS = { '+' : add_, '-' : sub_, '*' : mul_,
         '/' : div_, '%' : mod_, '^' : pwr_,
         '#' : sqr_, '\\': sqt_, '>' : gth_,
         '<' : lth_, '=' : eql_, '{' : bsl_,
         '}' : bsr_, '`' : len_, u'Σ': sum_,
         u'Π': rmp_, '!' : fac_, u'π': spi_, }
