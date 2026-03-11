pa = float(input("informe o valor: "))
pf = float(input("informe o valor: "))

pe = (pf - pa)
if(pe > 0 ):
	print("saldo positivo")
elif(pe < 0):
	print("saldo negativo")
elif(pe == 0):
	print("sem variacao")
else:
	print(round(pe, 2))