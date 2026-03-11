x = float(input("Número real: ")) 
k = int(input("Termos da série: "))

cont = 1
soma = 0
cima = 1
baixo = 1

while cont < k:
	soma = soma + (x**cima)/(baixo)
	cima = cima + 2
	baixo = baixo + 2
	cont = cont + 1


print(round(soma, 7))