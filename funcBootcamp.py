lyst=[]
x=True
def isBinary(lyst):
    for n in lyst:
        if n == 1 or n==0:
            x=True
        else:
            x=False
    return(x)
    
def isBinary2(lyst,allowNone):
    if allowNone==True:
        for n in lyst:
            if n == 1 or n==0 or n==None:
                x=True
            else:
                return(False)
    
    else:
        for n in lyst:
            if n == 1 or n==0:
                x=True
            else:
                return(False)
    return(x)
   
def calculateBinary(lyst):
    count=0
    countNone=0
    propop=0
    length=0
    if isBinary2(lyst,True)==True:
        for n in lyst:
            if n==1:
                count=count+1
            if n==None:
                countNone=countNone+1
        length=len(lyst)-countNone
        propop=float(count)/length
        return(propop)
    else:
        return("list is not binary")
        
        
        
