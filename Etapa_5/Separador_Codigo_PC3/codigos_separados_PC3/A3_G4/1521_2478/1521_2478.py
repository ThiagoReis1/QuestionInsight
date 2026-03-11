from math import *
n = int(input("capacidade de transportar containers: "))
i = int(input("estoque inicial: "))
q = int(input("novos containers: "))
cont = 0
sem = 0
conta = i
while(conta > 0):
	conta = conta -n + q
	cont += 1
print(cont)		
		