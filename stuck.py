import sys
import stuck_base
import stuck_math

allnums  = '0123456789.'
cmd_dict = {}

def push_num_lit(a,l,s):
    if '.' in l: s += [float(l)]
    else: s += [int(l)]
    a = False
    l = ''

def process(prog):
    stack = []
    num_lit   = ''
    num_lit_a = False
    if prog[-1] in allnums:
        prog += ' '
    for char in prog:
        if char in stuck_math.CMDS:
            if num_lit_a == True:
                push_num_lit(num_lit_a, num_lit, stack)
            stuck_math.CMDS[char](stack)
        if char in stuck_base.CMDS:
            if num_lit_a == True:
                push_num_lit(num_lit_a, num_lit, stack)
            stuck_base.CMDS[char](stack)
        elif char == ' ':
            if num_lit_a == True:
                push_num_lit(num_lit_a, num_lit, stack)
        elif char in allnums:
            num_lit_a = True
            num_lit  += char
    o = []
    for item in stack:
        if int(item) == item: o += [int(item)]
        elif float(item) == item: o += [float(item)]
        elif str(item) == item: o += [str(item)]
    print 'Stack:',`o`
    print ''.join(map(str,o))
        

def main():
    if len(sys.argv) < 2:
        while True:
            prog = raw_input("stuck > ")
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
