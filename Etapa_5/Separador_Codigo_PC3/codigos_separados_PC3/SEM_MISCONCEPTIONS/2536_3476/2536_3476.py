c = float(input())
d = float(input())
m = float(input())
juros = float(input())
juros = juros/100
mes = 0
saldo=d
if(c > 0 and d > 0 and m > 0 and juros > 0):
	while(saldo<c):
		saldo = saldo + (juros*saldo)
		saldo = saldo + m
		mes = mes + 1
	print(mes)
else:
	print("Dados incorretos")