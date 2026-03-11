from numpy import *

frase = input("entre com palavras: ").upper().split(',')

saida = zeros(6,dtype=int)
maior = 0 

for i in frase:
	if i == "MC":
		saida[0] += 1
	elif i == "C":
		saida[1] += 1
	elif i == "CM":
		saida[2] += 1
	elif i == "EM":
		saida[3] += 1
	elif i == "E":
		saida[4] += 1 
	elif i == "ME":
		saida[5] += 1
		
for i in saida:
	if i > maior:
		maior = i
print(maior)
print(saida)
		
