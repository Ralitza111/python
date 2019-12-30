import numpy as np
def findOL(arryMatx):
    x=np.median(arryMatx,axis=1)
    arryMatx=arryMatx.transpose()
    diff=np.absolute(arryMatx-x)
    diff=diff.transpose()
    index=np.argmax(diff,axis=1)
    return index



def main():
    firstMatx = np.array([[10,3,2],[1,2,6]])	
    print(findOL(firstMatx))

    thirdMatx = np.array([[1,10,2,8,5],[2,7,3,9,11],[19,2,1,1,5]])
    print(findOL(thirdMatx))
    
    thirdMatx = np.array([[1,10,8,5],[7,3,9,11],[19,1,1,5]])
    print(findOL(thirdMatx))
    
 	
main()
