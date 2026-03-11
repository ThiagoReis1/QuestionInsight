from numpy import*
notas = array(eval(input()))
i=0
peso= [4, 3]
np = sum(notas*peso)/sum(peso)
print(round(np,2))