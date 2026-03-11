a = float(input("abertura: "))
b = float(input("fechamento: "))

if( a<b):
	print("saldo positivo")
elif(a>b):
	print("saldo negativo")
else:
	print("sem variacao")