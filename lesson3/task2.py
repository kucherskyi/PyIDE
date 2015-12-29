
def string_format(*args,**kwargs):
    
    ar = ','.join([str(arg) for arg in args])
    kwar = ','.join(['%s=%s'% (key,value) for key, value in kwargs.items()])
    print '{}\n{}'.format(ar, kwar)
    
    
        
        
string_format(123123,"asdasdaaa", key ='value', ke22y ='value222')