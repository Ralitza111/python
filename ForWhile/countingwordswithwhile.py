import os 
setdir=os.chdir("C:\Users\Ralitza\OneDrive - Seattle University\SeattleU\IS 5201\week1&2")
count=0
while True:
    EnterFile=raw_input("Please Enter file name(Enter x if you want to exit)")
    f=open(EnterFile,"r")
    for words in f:
        words=words.split()
        count=count+len(words)
    print(count)
        