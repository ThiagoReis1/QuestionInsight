from numpy import *

vetor = (input("Informe as siglas dos paises: ")).split(',')
qtd = zeros(5,dtype=int)

for i in range(size(vetor)):
	if vetor[i] == "BE":
		qtd[0] = qtd[0] + 1
	elif vetor[i] == "ES":
		qtd[1] = qtd[1] + 1
	elif vetor[i] == "FR":
		qtd[2] = qtd[2] + 1
	elif vetor[i] == "IT":
		qtd[3] = qtd[3] + 1
	elif vetor[i] == "PT":
		qtd[4] = qtd[4] + 1
		
print(max(qtd))
print(qtd)

