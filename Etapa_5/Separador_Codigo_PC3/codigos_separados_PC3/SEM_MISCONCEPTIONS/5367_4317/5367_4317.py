from numpy import *

cpf = array(eval(input("Digite o vetor: ")))
aux = [1,2,3,4,5,6,7,8,9]
total_soma = 0

for i in aux:
	cpf[i] = cpf[i] * aux[i]

print (total_soma%11)
