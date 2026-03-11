p = int(input("p: "))

cont = 0
soma = 0

while (p != 0):
	
	if (p == 1):
		pontos = 20
	elif (p == 2):
		pontos = 15
	elif (p == 3):
		pontos = 10
	elif (p >= 4 and p <= 10):
		pontos = 11 - p
	else:
		pontos = 0
	soma = soma + pontos
	cont = cont + 1
	p = int(input("p: "))
print(soma)