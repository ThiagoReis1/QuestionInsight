pa = float(input("Preco: "))
pf = float(input("Preco: "))

total = pf - pa

if(total > 0):
	print("saldo positivo")
elif(total == 0):
	print("sem variacao")
elif(total < 0):
	print("saldo negativo")