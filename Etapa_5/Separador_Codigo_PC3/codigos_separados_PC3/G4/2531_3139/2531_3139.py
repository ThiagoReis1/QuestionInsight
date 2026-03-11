v = float(input("O valor do premio: "))
m = float(input("O valor do saque mensal: "))
i = float(input("A taxa de juros: "))


t = 0
saldo = v


if (v > 0) and (m > 0) and ( i > 0):
	while(saldo > v*0.1):
		round(saldo, 2)
		rend = saldo * i
		saldo = rend + saldo
		t = t + 1
		print(t)
else:
	print("Dados incorretos")
	

	
	
	
	
