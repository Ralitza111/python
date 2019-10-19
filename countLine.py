import os 
workDir=os.chdir("C:\Users\Ralitza\OneDrive - Seattle University\SeattleU\IS 5201\week1")

fileName=raw_input("Please enter the file name:")
sum=0
f=open(fileName,"r")
for words in f:
    wordline=words.strip()
    sum=sum+1
print("the length is", sum)
