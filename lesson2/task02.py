import sys

def fac(a):
    def inside_fac(a):
        if a == 0:
            return 1
        return inside_fac(a-1) * a
    print 'Factorial of %s is %s'% (a, inside_fac(a))


def my_args(*args):
    numbe = 0
    lis = []
    for ar in args:
        numbe +=1
        lis.append(ar)
        print '%s argument is %s' % (numbe, str(ar))
    print 'Or just list of them: %s' % (lis)


def harmony(*args):
    b = 0.0
    for ar in args:
        b += float(ar)

    print b/len(args)

fac(12)
my_args(12,'sad',11)
harmony(12,32)