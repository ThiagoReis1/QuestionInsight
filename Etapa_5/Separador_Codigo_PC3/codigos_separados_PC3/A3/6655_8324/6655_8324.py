from numpy import *
nota = array(eval(input("digite as notas: ")))
pesos = array([3,4,2,1,4,5])

total = sum(notas * pesos) / sum(pesos)
print(round(media,2))