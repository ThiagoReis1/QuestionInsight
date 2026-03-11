from numpy import*
notas = array(eval(input("digite as notas:")))
pesos = ([3,2,4,1,3])

total = sum(notas * pesos) / sum(pesos)

print(round(total, 2))