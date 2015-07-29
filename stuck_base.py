NAME    = 'Stuck Base'
VERSION = '1.0'
DESCR   = 'Base functions for the Stuck programming language.'

def add_(s): s += [s.pop(-2)+s.pop()]
def sub_(s): s += [s.pop(-2)-s.pop()]
def mul_(s): s += [s.pop(-2)*s.pop()]
def div_(s): s += [s.pop(-2)/s.pop()]
def mod_(s): s += [s.pop(-2)%s.pop()]
def pwr_(s): s += [s.pop(-2)**s.pop()]
def sqr_(s): s += [s.pop()**2]
def sqt_(s): s += [s.pop()**0.5]
def inp_(s): s += [float(input())]

CMDS = { '+' : add_, '-' : sub_, '*' : mul_,
         '/' : div_, '%' : mod_, '^' : pwr_,
         '#' : sqr_, '\\': sqt_, 'i' : inp_, }
