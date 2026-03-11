from numpy import*

dado = eval(input("digite o vetor de numeros indicando a faces do dado: "))

p_total = 0

for i in range(len(dado)):
	faces = dado[i]
	
	if faces == 1:
		p_total += 10 
		
	elif faces == 2:
		p_total += 5
		
	elif faces == 3:
		p_total += 0
		
	elif faces == 4:
		p_total  += 5
		
	elif faces == 5:
		p_total += 20
		
	elif faces == 6:
		p_total += 10
		
print(p_total)