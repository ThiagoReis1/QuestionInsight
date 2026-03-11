from numpy import*

contagem [0]*6

entrada = input().upper()
codigos = entrada.split(',')

for codigo in codigos:
	if codigo == "MC":
	   contagem[0] += 1
	elif codigo == "C":
	   contagem[1] += 1
	elif codigo == "CM":
	   contagem[2] += 1
	elif codigo == "EM":
	   contagem[3] += 1
	elif codigo == "E":
	   contagem[4] += 1
	elif codigo == "ME":
		contagem[5] += 1
	
		 
max_contagem = max(contagem)

print(max_contagem)
print(contagem)
