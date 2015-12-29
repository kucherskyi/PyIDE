
    
def return_values(sorce):
        
    pos = []
    named = []
    asd ={}
    #sorce = sorce.replace(' ', '')
    #print sorce
    for x in sorce.split('\n' ):
        for y in x.split(','):
            if '=' in y:
                z = y.split('=')
                named.append(z)
            else:
                pos.append(y)
    
    for c,v in named:
        asd[c] = v
    
    print 'Dict: %s \nTuple:  %s' % (asd, tuple(pos))
    
                
return_values('a123123,asdasdaaa \n ke22y=value222,key=value')
