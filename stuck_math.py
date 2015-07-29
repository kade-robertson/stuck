NAME    = 'Stuck Math'
VERSION = '1.0'
DESCR   = 'Basic math functions for the Stuck programming language.'

def len_(s): s += [((s.pop(-4)-s.pop(-2))**2+(s.pop(-2)-s.pop())**2)**0.5]

CMDS = { '`' : len_ }
