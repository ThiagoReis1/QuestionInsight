Var1=float(input("Peso da encomenda: "))
if(Var1<5000):
	valor=Var1*0.05
	print(round(valor,2))
else:
	taxa=60.00
	valor=Var1*0.04+taxa
	print(round(valor,2))