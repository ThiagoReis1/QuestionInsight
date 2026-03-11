a=float(input("a?"))
b=float(input("b"))

a=round(a,2)
b=round(b,2)

if(a<b):
	print("saldo positivo")
elif(a==b):
	print("sem variacao")
elif(a>b):
	print("saldo negativo")