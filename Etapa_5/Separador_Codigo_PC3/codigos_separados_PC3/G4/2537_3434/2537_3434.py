h = float(input("valor da heranca: "))
sm = float(input("saque mensal: "))
j = float(input("taxa de juros: "))/100

saldo = h + (h*j) - sm
mes = 0
print(saldo)
print(h+(h*2/10))
while (saldo <= h+(h*2/10)):
	saldo = saldo + (saldo*j) - sm
	mes = mes + 1
	print (mes)