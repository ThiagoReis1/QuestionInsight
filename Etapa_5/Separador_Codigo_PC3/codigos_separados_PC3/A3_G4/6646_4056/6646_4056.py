from numpy import*

n = array(eval(input("digite: ")))
i = 0
peso = [1,2,3]

mp = sum(n*peso)/sum(peso)
print(round(mp,2))