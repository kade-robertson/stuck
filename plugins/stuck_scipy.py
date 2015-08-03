# -*- coding: utf-8 -*-

NAME    = 'Stuck SciPy'
CREATOR = 'Kade Robertson'
VERSION = '1.0'
DESCR   = 'SciPy functions plugin for the Stuck programming language.'

import numpy
from scipy import linalg

def minv_(s):
    if type(s[-1]) is list:
        l = numpy.array(s.pop())
        k = linalg.inv(l)
        return s + [k.tolist()]

def mdet_(s):
    if type(s[-1]) is list:
        l = numpy.array(s.pop())
        k = linalg.det(l)
        return s + [k]

CMDS = { u'İ': minv_, u'Ɗ': mdet_ }
