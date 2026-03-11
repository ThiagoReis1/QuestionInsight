f = float(input("Digite salario: "))

print("Entrada: R$ " , f)

if (f > 0):
	a = f + ((f * 50)/100)
	al = round(a,2)
	print("Novo salario R$: ", al)