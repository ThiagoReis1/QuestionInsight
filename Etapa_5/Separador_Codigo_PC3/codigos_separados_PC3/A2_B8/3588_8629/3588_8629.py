vet = eval(input("pontuacao:"))

pontos = 10000

for i in vet:
	
	if i == 1:
		pontos = pontos*2
	
	elif i == 2:
		pontos = pontos
		
	elif i == 3:
		pontos = pontos/2
	
	elif i == 4:
		pontos = pontos/4
		
print(round(pontos,2))