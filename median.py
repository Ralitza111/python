import os 
import pandas as pd
setDir=os.chdir("C:\Users\Ralitza\OneDrive - Seattle University\SeattleU\IS 5201\week3")
InFile=open("numbers1.txt","r")
number=[]
median=0
for line in InFile:
    words=line.split(",")
    for words in words:
        number.append(int(words))
number.sort()
if (len(number)%2!=0):
        print(number[(int(round(len(number)/2)))])
else:
    median=float(number[(len(number)/2)]+number[((len(number)/2))-1])/2
    print((median))
    
        
        
    