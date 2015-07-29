NAME    = 'Stuck Base'
CREATOR = 'Kade Robertson'
VERSION = '1.1'
DESCR   = 'Base functions plugin for the Stuck programming language.'

def add_(s): s += [s.pop(-2)+s.pop()]
def sub_(s): s += [s.pop(-2)-s.pop()]
def mul_(s): s += [s.pop(-2)*s.pop()]
def div_(s): s += [s.pop(-2)/s.pop()]
def mod_(s): s += [s.pop(-2)%s.pop()]
def pwr_(s): s += [s.pop(-2)**s.pop()]
def gth_(s): s += [s.pop(-2)>s.pop()]
def lth_(s): s += [s.pop(-2)<s.pop()]
def eql_(s): s += [s.pop(-2)==s.pop()]
def bsl_(s): s += [float(int(s.pop(-2))<<int(s.pop()))]
def bsr_(s): s += [float(int(s.pop(-2))>>int(s.pop()))]
def sqr_(s): s += [s.pop()**2]
def sqt_(s): s += [s.pop()**0.5]
def inp_(s): s += [float(input())]
def inl_(s): s += [input()]
def pls_(s): s.pop()
def pal_(s):
    while len(s)>1:
        s.pop(0)
def flt_(s):
    l = s.pop(-1)
    while l:
        s += [l.pop(0)]

CMDS = { '+' : add_, '-' : sub_, '*' : mul_,
         '/' : div_, '%' : mod_, '^' : pwr_,
         '#' : sqr_, '\\': sqt_, 'i' : inp_,
         ';' : pls_, ',' : pal_, '>' : gth_,
         '<' : lth_, '=' : eql_, '{' : bsl_,
         '}' : bsr_, 'l' : inl_, '~' : flt_ }
