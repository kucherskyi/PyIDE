
import os
import stat
import datetime
import time
import sys

def folder_parser(folder):

    pathh = str(folder)
    for fi in os.listdir(pathh):
        filee = str(pathh + '\\' + fi)
        info = os.access(filee, os.R_OK)
        print fi
        print '%s file permissions: \n\
                exists - %s,\n\
                readeble - %s,\n\
                writeble - %s,\n\
                executible - %s' %\
                (fi, os.access(filee, os.R_OK),os.access(filee, os.W_OK),\
                os.access(filee, os.F_OK),os.access(filee, os.X_OK))
        if os.stat(filee).st_uid == 0:
            print '%s owner - root' % fi
        print 'Last modified on %s'\
               % datetime.datetime.fromtimestamp(int(os.stat(filee).st_mtime))
        print '-' * 80

if len(sys.argv)==2 and os.path.exists(sys.argv[1]) is True:
    folder_parser(str(sys.argv[1]))
elif len(sys.argv) == 0:
    folder_parser(os.path.dirname(os.path.realpath(__file__)))
elif os.path.exists(sys.argv[1]) is False:
    raise NameError('Directory doesn\'t exist')
elif len(sys.argv)>2:
     raise NameError( 'More arguments than needed')
else :
    raise NameError('Some error')