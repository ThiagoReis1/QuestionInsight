from numpy import*

n = array(eval(input("Notas ")))
i = 0
peso = [5,4,3,2]

mp = sum(n*peso)/sum(peso)
print(round(mp,2 ))