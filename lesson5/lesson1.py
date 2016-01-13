import re
from nt import write



def print_empty():
    out = open('alice01.txt', 'w')
    lines = 0
    for lin in open('alice.txt', 'r'):
        if re.match('\n', lin):
            lines +=1
        else:
            out.write(lin)
    print '%s empty lines were found!' % lines

#print_empty()

def remove_whitespace():
    out = open('alice02.txt', 'w')
    lines = 0
    for lin in open('alice.txt', 'r'):
        if re.match('\s', lin):
            out.write(lin.strip()+'\n')
            lines +=1
        else:
            out.write(lin)
            

    # print '%s lines with whitespace' % lines

if __name__ == '__main__':
    import timeit
    print timeit.timeit("remove_whitespace()", setup="from __main__ import remove_whitespace")
    



