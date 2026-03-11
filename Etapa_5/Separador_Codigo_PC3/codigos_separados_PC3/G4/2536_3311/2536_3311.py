c = float(input("Digite:"))
d = float(input("Digite:"))
m = float(input("Digite:"))
j = float(input("Digite:"))

if(c<=0 or d<=0 or m<=0 or j<=0):
	print("Dados incorretos")
else:
	mes=0
	saldo = d
	juros = j/100
	while(saldo < c):
		saldo = saldo * (1+juros)
		saldo = round(saldo + m,2)
		mes = mes + 1
		
	print(mes)