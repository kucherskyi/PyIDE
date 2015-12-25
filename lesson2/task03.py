import sys
import random
import datetime

class MyNumberPrinter(object):

    def __init__(self,num):
        self.num = num


    def me(self):
        print 'Original value is %s' % (self.num)


    def factorial(self):
        
        def inside_fac(val):
            if val == 0:
                return 1
            return inside_fac(val - 1) * val

        print 'Factorial of %s is %s' % (self.num, inside_fac(self.num))


    def string(self,text):
        
        print '%s value %s times is: %s' % (text,self.num,text*self.num)


    def update(self,new_value):
        self.num = new_value
        print 'New value is %s' % (self.num)

    def time_in_past(self,val):
        
        if val == 'd':
            literal = 'days'
            a = datetime.timedelta(days = self.num)
        elif val == 'm':
            literal = 'monts'
            a = datetime.timedelta(minutes = self.num)
        elif val == 'h':
            literal = 'hours'
            a = datetime.timedelta(hours = self.num)
        elif val == 's':
            literal = 'seconds'
            a = datetime.timedelta(seconds = self.num)

        vas_ago = datetime.datetime.now().replace(microsecond=0) - a

        print '%s %s ago vas : %s' %(self.num, literal,vas_ago)


my=MyNumberPrinter(5)

my.me()
my.factorial()
my.string('abc')
my.update(11)
my.time_in_past('d')


