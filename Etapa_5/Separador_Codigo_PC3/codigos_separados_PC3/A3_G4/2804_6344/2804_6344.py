di = int(input("Digite um numero: "))
meses = int(input("Digite os meses de aplicacao:" ))

cont = 0
taxa = 0.01
acum = 0
while(cont < meses):
	di = di + (di*taxa)
	cont = cont + 1
	print(round(di,2))
	