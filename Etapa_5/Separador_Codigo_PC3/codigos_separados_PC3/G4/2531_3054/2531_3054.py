V = float(input("premio da mega sena: "))
M = float(input("saque mensal fixo: "))
i = float(input("informe o juros: "))

mes = 1
saldo = V

while(saldo < 0.1 * V ):
	saldo = (saldo + (saldo * i) - M) * mes
	mes = mes + 1
if(V <0 ) and (M < 0) and (i< 0):
	print("Dados incorretos")
print(round(mes, 2))	
