from numpy import *
pesos = array([1, 2, 3])
notas = array(eval(input("Notas: ")))
i= 0

notas1= notas[0] * pesos[0]
notas2 = notas[1] * pesos [1]
notas3 = notas[2] * pesos[2]
notafinal = (notas1+notas2+notas3)/sum(pesos)
print(round(notafinal, 2))