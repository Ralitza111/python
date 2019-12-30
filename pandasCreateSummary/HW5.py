import os 
import pandas as pd 
import numpy as np
setDir=os.chdir("C:/Users/Ralitza/OneDrive - Seattle University/SeattleU/IS 5201/week6")

#df_titanic=pd.read_csv("titanic3.csv", sep=',', header=0)

def generateNumericSummary(dat, group):
    dat=pd.Series(dat)
    dat.numMissing=sum(np.isnan(dat))
    dat.means=dat.groupby([group]).mean()
    dat.std=dat.groupby([group]).std()
    dictionary = {
		"std" : dat.std,
		"numMissing" : dat.numMissing,
		"mean" : dat.means
	}
    return dictionary
    
def main():
    
    titanic=pd.read_csv("titanic3.csv", sep=',', header=0)
    result1 = generateNumericSummary(titanic['age'],titanic['survived'])
    print(result1)

    result2 = generateNumericSummary(titanic['fare'],titanic['survived']) 
    print("Number of missing values of 'fare' is "+str(result2['numMissing']))
    print("mean 'fare' by 'survived':") 
    print(result2['mean'])
    print("standard deviation of 'fare' by 'survived':") 
    print(result2['std'])
    
    result3 = generateNumericSummary(titanic['age'],titanic['pclass'])
    print(result3)

 	
main()