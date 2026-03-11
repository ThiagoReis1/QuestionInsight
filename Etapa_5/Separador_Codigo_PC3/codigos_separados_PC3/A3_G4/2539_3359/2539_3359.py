v = float(input("digite o valor do premio em RS: "))
m = float(input("digite o saque mensal fixo em RS: "))
j = float(input("digite a taxa de juros em porcentagem: "))


sal = 0
mes = 1
t =0
if ( v > 0 and m > 0 and j > 0):
	while (j != 0.2):
		sal = sal + mes
		mes = mes + 1
		print(v)
	
	
else:
	print("Dados incorretos")
	
	
	