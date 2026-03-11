from numpy import *

vetor= array(eval(input("vetor: ")))

contagem = zeros(len(vetor), dtype=int)
cont = 0

for i in vetor:
	if i != 0:
		contagem[cont] = i
		cont += 1
	
print(contagem)
