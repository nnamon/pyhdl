#!/bin/usr/python

def nandg(a, b):
    """primitive nand gate"""
    return not (a and b)

def notg(a):
    """not gate"""
    return nandg(a, a)

def andg(a, b):
    """and gate"""
    return notg(nandg(a, b))

def norg(a, b):
    """nor gate"""
    return andg(notg(a), notg(b))

def org(a, b):
    """or gate"""
    return notg(norg(a, b))

def xorg(a, b):
    """xor gate"""
    return andg(org(a, b), nandg(a, b))

def xnorg(a, b):
    """xnor gate"""
    return nandg(org(a, b), nandg(a, b))

def morg(*args):
    """multi or gate"""
    arg_no = len(args)
    if arg_no == 2:
        return org(args[0], args[1])
    elif arg_no < 2:
        raise Exception("Bad input")
    return org(args[0], morg(*args[1:]))

def mandg(*args):
    """multi and gate"""
    arg_no = len(args)
    if arg_no == 2:
        return andg(args[0], args[1])
    elif arg_no < 2:
        raise Exception("Bad input")
    return andg(args[0], mandg(*args[1:]))
    
    

def multiplexor(a, b, c):
    return

"""
a b c out
0 0 0 0
0 0 1 0
0 1 0 0
0 1 1 1
1 0 0 1
1 0 1 0
1 1 0 1
1 1 1 1

_      __     _
(abc + abc) + abc + abc
"""

def test_gate(gate, no_of_args):
    results = execute_gate(gate, no_of_args)
    print "Testing: %s." % gate.func_name
    print "-------------------------------"
    for i in results:
        for j in i[0]:
            print "%d " % j,
        print "|  %d" % i[1]
    print "-------------------------------\n"
        
    
def execute_gate(gate, no_of_args):
    test = []
    for i in generate_possibilities(no_of_args):
        test.append((i, gate(*i)))
    return test

def generate_possibilities(no_of_args):
    poss = []
    for i in range(0, 2**no_of_args):
        temp = []
        for j in range(0, no_of_args):
            current_mask = 2**j
            temp.insert(0, (0 if (current_mask & i == 0) else 1))
        poss.append(temp)
    return poss

def main():
    gates = [andg, nandg, norg, notg, org, xorg, xnorg]
    for i in gates:
        test_gate(i, i.func_code.co_argcount)

    mgate_test_max = 5
    mgate_test_min = 2
    mgates = [morg, mandg]
    for i in mgates:
        for j in range(mgate_test_min, mgate_test_max):
            test_gate(i, j)
        
    
if __name__ == "__main__":
    main()
