from numpy import*
notas = array(eval(input("inf nota:")))
i = 0
peso = [3,4,2,1,4,5]

mp = sum(notas*peso)/(3+4+2+1+4+5)
print(round(mp , 2))