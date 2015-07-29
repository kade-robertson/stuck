# -*- coding: utf-8 -*-

NAME    = 'Stuck Math'
CREATOR = 'Kade Robertson'
VERSION = '1.1'
DESCR   = 'Basic math functions plugin for the Stuck programming language.'

def len_(s): s += [((s.pop(-4)-s.pop(-2))**2+(s.pop(-2)-s.pop())**2)**0.5]
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

CMDS = { '`' : len_, u'Σ': sum_, u'Π': rmp_ }
