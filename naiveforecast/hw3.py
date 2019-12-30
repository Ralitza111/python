#Author:Ralitza Mondal
#HW3
#lyst=[]
def NaivePrediction (lyst,k):
    n=0
    l=0
    avg=0
    sum1=0
    count=0
    i=0
    abErr=0
    if k<len(lyst):
        for j in range (k, len(lyst)):
            n=sum(lyst[i:j])
            i=i+1
            if n >= float(k)/2:
                l=1
                abErr=abs(lyst[j]-l)
                sum1=sum1+abErr
                count=count+1
            else:
                l=0
                abErr=abs(lyst[j]-l)
                sum1=sum1+abErr
                count=count+1            
        avg=float(sum1)/count
        return avg
    else:
        return("k should be less than the number of observations")

def main():
    
    #print(NaivePrediction([1,0,1,0,1],3))
    print(NaivePrediction([1,0,1,0,1],2))
    print(NaivePrediction([1,0,1,0,1],3))
    print(NaivePrediction([1,0,1,0,1],5))
    print(NaivePrediction([1,0,1,0,1,1,1],3))
    print(NaivePrediction([1,0,1,0,1,1,1],4))
    
    #print(NaivePrediction([1,1,1,1,1],3))

    
main()
