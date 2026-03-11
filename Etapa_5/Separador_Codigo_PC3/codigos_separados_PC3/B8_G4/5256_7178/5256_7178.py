a = float(input("preco inicial: "))
b = float(input("preco final: "))

if ((a>0)and(b>0)):
	y = ("saldo positivo")
	print(y)
elif ((a<0)and(b<0)):
	y = ("saldo negativo")
	print(y)
elif ((a==0)and(b==0)):
	y = ("sem variação")
	print(y)