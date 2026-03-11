valor = float(input("qual valor da casa?"))
saldo = float(input("qual valor vc dispoe?"))
deposito= float(input("quanto deposita por mes?"))
juros= float(input("quanto e os juros?"))

mes = 1
if(valor>0 and saldo>0 and deposito>0 and juros>0):
	while(saldo < valor):
		lucro = deposito * juros
		saldo = saldo + lucro
		saldo = round(saldo,2) 
		mes = mes + 1
	print(mes)
else:
	print("Dados incorretos")

	