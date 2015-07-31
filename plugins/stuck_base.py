NAME    = 'Stuck Base'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Base functions plugin for the Stuck programming language.'

import pprint

def inp_(s): return s + [input()]
def ins_(s): return s + [raw_input()]
def itk_(s): return s + [eval(x) for x in raw_input().split('|')]
def pls_(s): s.pop()
def tca_(s): return s + [map(ord,s.pop())]
def dup_(s): return s + [s[-1]]
def evl_(s): return s + [eval(s.pop())]
def rge_(s): return s + [range(s.pop())]
def rgi_(s): return s + [range(1,s.pop()+1)]
def ppt_(s): pprint.pprint(s[-1])
def map_(s):
    l = s.pop(-2)
    la = s.pop()
    if ':' not in la:
        return s + [map(eval(la),l)]
    else:
        return s + [map(eval('lambda '+la),l)]
def fil_(s):
    l = s.pop(-2)
    la = s.pop()
    if ':' not in la:
        return s + [filter(eval(la),l)]
    else:
        return s + [filter(eval('lambda '+la),l)]
def rot_(s):
    return [s[-1]]+s[:-1]
def rbw_(s):
    return s[1:]+[s[0]]
def zip_(s):
    if type(s[-1]) is int:
        l = []
        k = s.pop()
        while k:
            l = [s.pop()] + l
            k -= 1
        return s + [zip(*l)]
    else:
        return s + [zip(s.pop(-2),s.pop())]
def zpl_(s):
    if type(s[-1]) is int:
        l = []
        k = s.pop()
        while k:
            l = [s.pop()] + l
            k -= 1
        return s + [map(None,*l)]
    else:
        return s + [map(None,s.pop(-2),s.pop())]
def tst_(s):
    if type(s[-1]) is list:
        return s + [''.join(map(chr,s.pop()))]
    else:
        sr = ''
        while s: sr += chr(s.pop(0)) 
        return s + [sr]
def pal_(s):
    while len(s)>1:
        s.pop(0)
    return s
def flt_(s):
    if type(s[-1]) is list or type(s[-1]) is tuple:
        l = s.pop(-1)
        return s + [x for x in l]
def trn_(s):
    c = s.pop(-3)
    t,f = s.pop(-2),s.pop()
    if c: return s + [t]
    else: return s + [f]
def swp_(s):
    a,b = s.pop(-2),s.pop()
    return s + [b] + [a]
        
CMDS = { 'i' : inp_, '.' : pls_, ',' : pal_,
         '~' : flt_, 's' : ins_, '?' : trn_,
         't' : itk_, ';' : swp_, 'c' : tca_,
         'd' : tst_, 'z' : zip_, 'Z' : zpl_,
         '_' : dup_, '@' : rot_, 'e' : evl_,
         'r' : rge_, 'R' : rgi_, 'p' : ppt_,
         'm' : map_, 'f' : fil_, 'u' : rbw_,}
