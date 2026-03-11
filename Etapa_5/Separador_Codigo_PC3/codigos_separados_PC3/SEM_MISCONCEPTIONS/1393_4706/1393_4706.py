peso=float(input("Peso(g) "))
if(peso<5000):
	valor=peso*0.05
else:
	valor=peso*0.04+60
print(round(valor,2))