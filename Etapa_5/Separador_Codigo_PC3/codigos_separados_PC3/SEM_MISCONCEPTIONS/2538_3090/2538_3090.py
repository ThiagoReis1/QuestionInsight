s = float(input("valor do sitio:"))
d = float(input("valor inicial depositado:"))
m = float(input("deposito mensal fixo:"))
j = float(input("taxa de juros:"))/100
saldo = 0 
meses = 1
if((s > 0) and (d > 0) and (m > 0) and (j > 0)):
	while(saldo >= s):
		saldo = d + m * j
		meses = meses + 1
          print(meses)
else:
	print("Dados incorretos")
