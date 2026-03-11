V = float(input("valor da premiacao: "))
M = float(input("valor do saque realizado ao mes: "))
j = float(input("valor do juros ao mes: "))
mes = 0
VF=round((V+(V*10/100)),2)

if((V>0) and (M>0) and (j>0)):
	while(V<VF):
		V = round((V - M) + (V*j/100),2)
		mes = mes + 1
	print(mes)		
else:
	print("Dados incorretos")
		
