vini=float(input("bolsa no inicio"))
vfin=float(input("bolsa no final"))
x=vini-vfin
if(x<0):
	print("saldo positivo")
elif(x>0):
	print("saldo negativo")
else:
	print("sem variacao")