
import os
import stat
import datetime
import time

def folder_parser(folder):

    pathh = str(folder)
    for fi in os.listdir(pathh):
    
        filee = str(pathh + '\\' + fi)
        info = os.access(filee, os.R_OK)
    
        print fi
        print '%s file permissions: exists - %s, readeble - %s, writeble - %s, executible - %s' %\
                 (fi, os.access(filee, os.R_OK), os.access(filee, os.W_OK),\
                  os.access(filee, os.F_OK), os.access(filee, os.X_OK))
        if os.stat(filee).st_uid == 0:
            print '%s owner - root' % fi
    
        print 'Last modified on %s' % datetime.datetime.fromtimestamp(int(os.stat(filee).st_mtime))
        print '-----' * 5

folder_parser('C:\Users\Artem_Kucherskyi@epam.com\git\pytrain')