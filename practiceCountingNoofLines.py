import os 
workDir=os.chdir("C:\Users\Ralitza\OneDrive - Seattle University\SeattleU\IS 5201\week1")
count=0
fileName=raw_input("Please enter the file name:")
f=open(fileName,"r")
for wordline in f:
    lines=wordline.split()
    count=count+1
print("The number of words are" , count)