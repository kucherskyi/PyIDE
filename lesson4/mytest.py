import os
import stat
import datetime
import time
import sys

def list_files(startpath):
    file = open('name.txt','w')
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        file.write('{}{}\n'.format(indent, os.path.basename(root)))
        subindent = '_' * 4 * (level + 1)
        for f in files:
            file.write('{}{}\n'.format(subindent, f))
        

list_files('C:\Users\Artem_Kucherskyi@epam.com\git\pytrain')
