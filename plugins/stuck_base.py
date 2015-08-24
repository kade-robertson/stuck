NAME    = 'Stuck Base'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Base functions plugin for the Stuck programming language.'

import zlib
import base64

base36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def inp_(s): return s + [input()]
def ins_(s): return s + [raw_input()]
def itk_(s): return s + [eval(x) for x in raw_input().split('|')]
def pls_(s): s.pop(); return s
def tca_(s): return s + [map(ord,s.pop())]
def dup_(s): return s + [s[-1]]
def evl_(s): return s + [eval(s.pop())]
def rge_(s):
    if type(s[-1]) is list and len(s[-1])==2:
        return s + [range(*s.pop())]
    else:
        return s + [range(s.pop())]
def rgi_(s):
    if type(s[-1]) is list and len(s[-1])==2:
        a1, a2 = s.pop()
        return s + [range(a1, a2+1)]
    else:
        return s + [range(1,s.pop()+1)]
def ppt_(s): print s[-1]; return s
def wrp_(s): return [s]
def pnl_(s): return s + ["\n"]
def bas_(s):
    v = s.pop()
    if type(v) is str:
        return s + [base64.b64encode(v)]
    elif type(v) is int:
        t = s.pop()
        o = ''
        while t:
            t,b = divmod(t,v)
            o = base36[b] + o
        return s + [int(o) if v == 10 else o]
def bsc_(s):
    v = s.pop()
    if type(v) is str:
        return s + [base64.b64decode(v)]
def cmp_(s):
    k = s.pop()
    return s + [zlib.compress(k,9)]
def dmp_(s):
    k = s.pop()
    return s + [zlib.decompress(k)]
def rpl_(s):
    w = s.pop()
    k = s.pop()
    ss = s.pop()
    return s + [ss.replace(k,w)]
def lnn_(s):
    if type(s[-1]) is list or type(s[-1]) is str:
        return s + [len(s.pop())]
    else:
        return [len(s)]
def sjn_(s):
    j = s.pop()
    if type(j) is list:
        return s + [''.join(map(str,j))]
    elif type(j) is str:
        if type(s[-1]) is list:
            k = s.pop()
            return s + [j.join(map(str,k))]
        else:
            return [j.join(map(str,s))]
def map_(s):
    l = s.pop(-2)
    la = s.pop()
    if ':' not in la:
        return s + [map(eval(la),l)]
    else:
        return s + [map(eval('lambda '+la),l)]
def fil_(s):
    k = s.pop()
    if type(k) is list:
        if type(s[-1]) is list:
            v = s.pop()
            o = []
            for a,b in zip(v,k):
                if b: o += [a]
            return s + [o]
    elif type(k) is str:
        l = s.pop()
        if ':' not in l:
            return s + [filter(eval(k),l)]
        else:
            return s + [filter(eval('lambda '+k),l)]
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
def trs_(s): return s + [[list(x) for x in zip(*s.pop())]]
def rle_(s):
    v = s.pop()
    count = 1
    prev = ''
    lst = []
    for character in v:
        if character != prev:
            if prev:
                entry = (count, prev)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (count, character)
        lst.append(entry)
    return s + [[list(x) for x in lst]]
def ule_(s):
    l = s.pop()
    q = ""
    for character, count in l:
        q += character * count
    return s + [q]
def srt_(s):
    k = s.pop()
    if type(k) is list or type(k) is tuple:
        return s + [sorted(k)]
    elif type(k) is str:
        return s + [''.join(sorted(k))]
def get_(s):
    k = s.pop()
    l = s.pop()
    return s + [l[k]]
def fnd_(s):
    k = s.pop()
    l = s.pop()
    if k in l:
        return s + [l.index(k)]
    else:
        return s + [-1]
def cln_(s):
    l = s.pop()
    l = [x for x in l if x]
    return s + [l]
def sct_(s):
    n = s.pop()
    l = s.pop()
    v = [l[i:i+n] for i in xrange(0,len(l),n)]
    return s + [v]
def rev_(s):
    k = s.pop()
    return s + [k[::-1]]
def enm_(s):
    k = s.pop()
    return s + [list(enumerate(k))]
def alp_(s):
    return s + [alpha]
def isa_(s):
    k = s.pop()
    if type(k) is str:
        return s + [''.join(filter(str.isalpha,k))]
    elif type(k) is list:
        return s + [filter(str.isalpha,k)]
def low_(s):
    k = s.pop()
    if type(k) is str:
        return s + [s.pop().islower()]
    elif type(k) is int:
        return s + [97 <= k <= 122]
def upp_(s):
    k = s.pop()
    if type(k) is str:
        return s + [s.pop().isupper()]
    elif type(k) is int:
        return s + [65 <= k <= 90]
        
CMDS = { 'i' : inp_, 'y' : pls_, ',' : pal_,
         ']' : flt_, 's' : ins_, '?' : trn_,
         't' : itk_, ';' : swp_, 'c' : tca_,
         'd' : tst_, 'z' : zip_, 'Z' : zpl_,
         '_' : dup_, '@' : rot_, '~' : evl_,
         'r' : rge_, 'R' : rgi_, 'p' : ppt_,
         'm' : map_, 'f' : fil_, 'u' : rbw_,
         '[' : wrp_, 'j' : sjn_, 'N' : pnl_,
         'l' : lnn_, 'Q' : rpl_, 'b' : bas_,
         'B' : bsc_, 'C' : cmp_, 'D' : dmp_,
         'T' : trs_, 'o' : rle_, 'O' : ule_,
         '$' : srt_, '&' : get_, 'I' : fnd_,
         'U' : cln_, 'K' : sct_, 'Y' : rev_,
         'E' : enm_, 'A' : alp_, 'a' : isa_,
         'w' : low_, 'W' : upp_ }
