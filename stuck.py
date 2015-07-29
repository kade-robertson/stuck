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
    str_lit   = ''
    str_lit_a = False
    is_debug  = False
    if prog[-2:] == '-d':
        prog = prog[:-2]
        is_debug = True
    if prog[-1] in allnums:
        prog += ' '
    for char in prog:
        if char in stuck_math.CMDS and not str_lit_a:
            if num_lit_a == True:
                stack += [float(num_lit)]
                num_lit = ''
                num_lit_a = False
            stuck_math.CMDS[char](stack)
        elif char in stuck_base.CMDS and not str_lit_a:
            if num_lit_a == True:
                stack += [float(num_lit)]
                num_lit = ''
                num_lit_a = False
            stuck_base.CMDS[char](stack)
        elif char == ' ' and not str_lit_a:
            if num_lit_a == True:
                stack += [float(num_lit)]
                num_lit = ''
                num_lit_a = False
        elif char == '"':
            if str_lit_a:
                stack += [str_lit]
                str_lit = ''
                str_lit_a = False
            else:
                str_lit_a = True
        elif char in allnums and not str_lit_a:
            num_lit_a = True
            num_lit  += char
        else:
            str_lit += char
        if is_debug:
            print 'Char:',char,'|','Stack:',`stack`
    if is_debug: print 'Stack:',`stack`
    print ''.join(map(str,stack))
        

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
