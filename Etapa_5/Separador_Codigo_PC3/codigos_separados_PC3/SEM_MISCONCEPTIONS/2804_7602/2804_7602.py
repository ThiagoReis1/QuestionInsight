deposito = float(input())
meses = int(input())

cont = 0
soma = deposito
while (meses > cont):
			
	soma = soma + 1/100*soma
	cont += 1
	print(round(soma,2))