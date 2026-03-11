x = float(input("preco abertura "))
y = float(input("preco fechamento "))

if(y > x):
	print("saldo positivo")
elif(x == y):
	print("sem variacao")
else:
	print("saldo negativo")