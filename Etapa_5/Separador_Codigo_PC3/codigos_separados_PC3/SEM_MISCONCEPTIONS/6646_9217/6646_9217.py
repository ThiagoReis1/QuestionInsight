from numpy import *
vetor = array(eval(input("Digite as notas: ")))
pesos = array([1,2,3])

total = sum(vetor * pesos) / sum(pesos)
print(round(total, 2)) 