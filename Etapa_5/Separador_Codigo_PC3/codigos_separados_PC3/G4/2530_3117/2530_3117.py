d = float(input("d: "))
tf = float(input("tf: "))
j = float(input("j: ")) / 100

if d > 0 and tf > 0 and j > 0:
	mes = 0
	saldo = d
	
	while saldo - d <= d * 0.15:
		taxa = saldo * j
		saldo = (saldo + taxa) - tf
		saldo = round(saldo,2)
		mes = mes + 1
	
	print(mes)
else:
	print("Dados incorretos")