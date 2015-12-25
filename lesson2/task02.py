import sys

def fac(a):
    if a == 0:
        return 1
    return fac(a-1) * a
    
# print fac(int(sys.argv[1])) 

def prin(*args):
    for ar in args:
        return ar
        
# print prin(sys.argv[1:])

def medi(*args):
    b = 0.0
    for ar in args:
        for elem in ar:
            b += float(elem)
    
    
        
    print b/len(args)
    

fac(sys.argv[1])
prin(sys.argv[1:])
medi(sys.argv[1:])