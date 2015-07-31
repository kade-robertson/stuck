NAME    = 'Stuck Interpreter'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Interpreter for the Stuck programming language.'

import imp
import sys
import glob
from os.path import join,basename,splitext

allnums  = '0123456789ABCDEF.'
cmd_dict = {}

def import_modules(dr):
    return dict(_load(path) for path in glob.glob(join(dr,'[!_]*.py')))

def _load(path):
    name, ext = splitext(basename(path))
    return name, imp.load_source(name, path)

def det_num_type(nm):
    if '.' in nm: return float(nm)
    elif any(x in nm for x in 'ABCDEF'): return int(nm,16)
    else: return int(nm)

def process(prog):
    stack = []
    num_lit   = ''
    num_lit_a = False
    str_lit   = ''
    str_lit_a = False
    is_debug  = False
    plugins  = import_modules('plugins')
    if prog[-2:] == '-d':
        prog = prog[:-2]
        is_debug = True
    if prog[-1] in allnums:
        prog += ' '
    for char in prog:
        for plugin in plugins:
            if char in plugins[plugin].CMDS and not str_lit_a:
                if num_lit_a == True:
                    stack += [det_num_type(num_lit)]
                    num_lit = ''
                    num_lit_a = False
                stack = plugins[plugin].CMDS[char](stack)
        if char == ' ' and not str_lit_a:
            if num_lit_a == True:
                stack += [det_num_type(num_lit)]
                num_lit = ''
                num_lit_a = False
        elif char == '"':
            if str_lit_a:
                stack += [str_lit]
                str_lit = ''
                str_lit_a = False
            else:
                if num_lit_a:
                    stack += [det_num_type(num_lit)]
                    num_lit = ''
                    num_lit_a = False
                str_lit_a = True
        elif char in allnums and not str_lit_a:
            num_lit_a = True
            num_lit  += char
        elif str_lit_a:
            str_lit += char
        if is_debug: print 'Char:',char,'|','Stack:',`stack`
    if is_debug: print 'Stack:',`stack`
    print ''.join(map(str,stack))
        

def main():
    if len(sys.argv) < 2:
        while True:
            prog = raw_input("stuck > ")
            if prog == 'plugin':
                r=import_modules('plugins')
                for k in r:
                    print '%s - Version %s - By %s\n   %s'%(r[k].NAME, r[k].VERSION, r[k].CREATOR, r[k].DESCR)
            elif prog == '':
                print 'Hello, World!'
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
