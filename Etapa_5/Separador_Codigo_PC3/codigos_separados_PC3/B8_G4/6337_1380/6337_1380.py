from numpy import *

vet = array(eval(input("Informe o vetor: ")))
n = int(input("Informe o valor de n: "))
saida_pos = ""
cont = 0

for i in range(size(vet)):
	
	if (vet[i] == n):
		saida_pos += "\n" + str(i)
	elif (vet[i] < n):
		cont += 1
		
print(saida_pos)
print(cont)