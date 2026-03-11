atual = float(input("Salario atual: "))
print("Entrada: R$", atual)

if ( atual > 0 ):
	if( atual <= 800 ):
		y = atual + ( atual/100 * 50) #50%
	elif( atual <= 1000 ):
		y = atual + ( atual/100 * 40) #40%
	elif( atual <= 1200 ):
		y = atual + ( atual/100 * 30) #30%
	elif( atual <= 1400 ):
		y = atual + ( atual/100 * 20) #20%
	elif( atual <= 1600 ):
		y = atual + ( atual/100 * 10) #10%
	elif( atual > 1600 ):
		y = atual + ( atual/100 * 5) #5%
	print("Novo salario: R$", round(y, 2))
else:
	print("Dado invalido")