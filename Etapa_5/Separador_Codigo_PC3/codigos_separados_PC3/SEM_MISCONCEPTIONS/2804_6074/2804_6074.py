deposito = float(input())
n =float(input())

juros = 1
x = 0

while(x < n):
	deposito = deposito + (deposito * (juros/100))
	x = x + 1
	print(round(deposito,2))