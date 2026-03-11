from numpy import *
notas = array(eval(input("Notas: ")))
i = 0
num = 0
pesos = ([1, 2, 3])
conta = notas * pesos
numerador = sum(conta) / sum(pesos)
print(round(numerador , 2))