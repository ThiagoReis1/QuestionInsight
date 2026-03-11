v = float(input("reais:"))
m = float(input("saque mensal;"))
j = float(input("taxa de juros:"))/100

t = 0
saldo = v

if(v > 0 and m > 0 and j > 0):
	while (saldo <= v+v*(20/100)):
		saldo = round((saldo + saldo*j) - m, 2)
		t = t + 1
	
	print(t)		
else:
	print("Dados incorretos")		
	
		

	