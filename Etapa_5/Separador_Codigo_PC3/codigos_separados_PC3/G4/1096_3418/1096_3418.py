#ENTRADA
from math import*

nf = int(input("Valor fornecido: "))

#CALCULO

n1 = nf // 10000
r1 = nf % 10000
n2 = r1 // 100
n3 = nf % 100

calculo = ((n1)**3)+((n2)**3)+((n3)**3)

if(nf == calculo):
	print("atende")
	print(nf)
else:
	print("nao atende")
	print(nf)