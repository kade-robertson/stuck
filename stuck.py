NAME    = 'Stuck Interpreter'
CREATOR = 'Kade Robertson'
VERSION = '1.0'
DESCR   = 'Interpreter for the Stuck programming language.'

import sys
import stuck_base
import stuck_math

allnums  = '0123456789.'
cmd_dict = {}

def process(prog):
    stack = []
    num_lit   = ''
    num_lit_a = False
    is_debug  = False
    if prog[-2:] == '-d':
        prog = prog[:-2]
        is_debug = True
    if prog[-1] in allnums:
        prog += ' '
    for char in prog:
        if char in stuck_math.CMDS:
            if num_lit_a == True:
                stack += [float(num_lit)]
                num_lit = ''
                num_lit_a = False
            stuck_math.CMDS[char](stack)
        elif char in stuck_base.CMDS:
            if num_lit_a == True:
                stack += [float(num_lit)]
                num_lit = ''
                num_lit_a = False
            stuck_base.CMDS[char](stack)
        elif char == ' ':
            if num_lit_a == True:
                stack += [float(num_lit)]
                num_lit = ''
                num_lit_a = False
        elif char in allnums:
            num_lit_a = True
            num_lit  += char
        if is_debug:
            print 'Char:',char,'|','Stack:',`stack`
    o = []
    for item in stack:
        if type(item) is not list and int(item) == item: o += [int(item)]
        elif type(item) is not list and float(item) == item: o += [float(item)]
        elif type(item) is not list and str(item) == item: o += [str(item)]
        elif type(item) is list: o += [item]
    print 'Stack:',`o`
    print ''.join(map(str,o))
        

def main():
    if len(sys.argv) < 2:
        while True:
            prog = raw_input("stuck > ")
            if prog == 'plugin':
                for k in [stuck_base, stuck_math]:
                    print '%s - Version %s - By %s\n   %s'%(k.NAME, k.VERSION, k.CREATOR, k.DESCR)
            else:
                process(prog)
    else:
        if sys.argv[1].split('.')[-1] == 'stk':
            f = open(sys.argv[1], 'r')
            prog = f.read()
            process(prog)
        else:
            print 'Usage: python',__file__.split('/')[-1],'program.stk'

if __name__ == '__main__':
    main()
