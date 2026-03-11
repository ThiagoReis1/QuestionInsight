from numpy import *

frase = input("entre com um estado: ").split(",")

contagem = zeros(5, dtype=int)

for i in frase:
	if i == 'AC':
		contagem[0] = contagem[0] + 1
	elif i == 'AM':
		contagem[1] = contagem[1] + 1
	elif i == "PA":
		contagem[2] = contagem[2] + 1
	elif i == "RO":
		contagem[3] = contagem[3] + 1
	elif i == "RR":
		contagem[4] = contagem[4] + 1
	
print(max(contagem))	
print(contagem)




