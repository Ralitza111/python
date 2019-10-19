import os 
#import pandas as pd
setDir=os.chdir("C:\Users\Ralitza\OneDrive - Seattle University\SeattleU\IS 5201\week3")
InFile=open("lab3.txt","r")
lyst=[]
for line in InFile:
    words=line.split()
    for word in words:
        word=word.upper()
        lyst.append(word)
print(lyst)

theDictionary={}

for word in lyst:
    if not word in theDictionary:
         theDictionary[word]= 1
    else:
        theDictionary[word]+=1
print(theDictionary)

maxNum=max(theDictionary.values())

for key,value in theDictionary.items():
    if value==maxNum:
        print("Mode is " + str(key) + " with frequency " + str(maxNum))
