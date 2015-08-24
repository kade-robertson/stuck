# -*- coding: utf-8 -*-

NAME    = 'Stuck Interpreter'
CREATOR = 'Kade Robertson'
VERSION = '1.2'
DESCR   = 'Interpreter for the Stuck programming language.'

import imp
import sys
import glob
from os.path import join,basename,splitext

allnums = '0123456789.'
cmd_dict = {}

def import_modules(dr):
    return dict(_load(path) for path in glob.glob(join(dr,'[!_]*.py')))

def _load(path):
    name, ext = splitext(basename(path))
    return name, imp.load_source(name, path)

def det_num_type(nm):
    if '.' in nm: return float(nm)
    else: return int(nm)

def process(prog, stack=[], saved_v=[], t=0, nest=0):
    saved_v   = []
    num_lit   = ''
    num_lit_a = False
    str_lit   = ''
    str_lit_a = False
    is_debug  = False
    plugins   = import_modules('plugins')
    imp_print = True
    char_mode = False
    if prog[-2:] == '-d':
        prog = prog[:-2]
        is_debug = True
    if prog[-1] in allnums:
        prog += ' '
    for char in prog:
        if char_mode:
            stack += [char]
            char_mode = False
            continue
        for plugin in plugins:
            if char in plugins[plugin].CMDS and not str_lit_a:
                if char == 'p':
                    imp_print = False
                if num_lit_a == True:
                    stack += [det_num_type(num_lit)]
                    num_lit = ''
                    num_lit_a = False
                stack = plugins[plugin].CMDS[char](stack)
        if char == "'" and not str_lit_a:
            if num_lit_a == True:
                stack += [det_num_type(num_lit)]
                num_lit = ''
                num_lit_a = False
            char_mode = True
        if char == 'g' and not str_lit_a:
            if num_lit_a == True:
                stack += [det_num_type(num_lit)]
                num_lit = ''
                num_lit_a = False
            saved_v += [stack[-1]]
        elif char == 'G' and not str_lit_a:
            if num_lit_a == True:
                stack += [det_num_type(num_lit)]
                num_lit = ''
                num_lit_a = False
            idx = stack.pop()
            stack += [saved_v[idx]]
        if char == ':' and not str_lit_a:
            if type(stack[-2]) is list:
                _prog = stack.pop()
                if 'p' in _prog:
                    imp_print = False
                stack += [[process(_prog,stack=[x],saved_v=saved_v,t=2,nest=nest+1) for x in stack.pop()]]
            else:
                _prog = stack.pop()
                stack = [process(_prog,stack=[x],saved_v=saved_v,t=2,nest=nest+1) for x in stack]
        if char == 'V' and not str_lit_a:
            if num_lit_a == True:
                stack += [det_num_type(num_lit)]
                num_lit = ''
                num_lit_a = False
            times = stack.pop()
            oper = stack.pop()
            tomod = stack
            if 'p' in oper:
                imp_print = False
            for i in range(times):
                tomod = process(oper,stack=tomod,saved_v=saved_v,t=1,nest=nest+1)
            stack = tomod
        if char == 'h' and not str_lit_a:
            toeval = stack.pop()
            condition = stack.pop()
            value = stack.pop()
            if 'p' in toeval or 'p' in condition:
                imp_print = False
            while process(condition,stack=[value],saved_v=saved_v,t=2,nest=nest+1):
                value = process(toeval,stack=[value],saved_v=saved_v,t=2,nest=nest+1)
            stack += [value]
        if char == ' ' and not str_lit_a:
            if num_lit_a == True:
                stack += [det_num_type(num_lit)]
                num_lit = ''
                num_lit_a = False
        elif char == '"':
            if str_lit_a:
                stack += [str_lit.replace("''",'"')]
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
        if is_debug: print '> '*nest+'Char:',char,'|','Stack:',`stack`
    if is_debug: print '> '*nest+'Stack:',`stack`
    if t == 0:
        if imp_print:
            print ''.join(map(str,stack))
    else:
        if t == 1:
            return stack
        elif t == 2:
            return stack[0]
        

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
                process(prog, stack=[], t=0, nest=0)
    else:
        if sys.argv[1].split('.')[-1] == 'stk':
            f = open(sys.argv[1], 'r')
            prog = f.read()
            if prog == 'plugin':
                r=import_modules('plugins')
                for k in r:
                    print '%s - Version %s - By %s\n   %s'%(r[k].NAME, r[k].VERSION, r[k].CREATOR, r[k].DESCR)
            elif prog == '':
                print 'Hello, World!'
            else:
                process(prog, stack=[], t=0, nest=0)
        else:
            print 'Usage: python',__file__.split('/')[-1],'program.stk'

if __name__ == '__main__':
    main()
