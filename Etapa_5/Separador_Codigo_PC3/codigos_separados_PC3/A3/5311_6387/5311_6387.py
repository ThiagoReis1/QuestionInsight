a = float(input("Deposito inicial: "))
b = int(input("Numero de meses: "))

juros = 1.2
t = 1 
soma = 0
saldo = a 

while (t <= b):
	saldo = saldo + saldo * 0.012
	t = t + 1 
	print(round(saldo,2))
