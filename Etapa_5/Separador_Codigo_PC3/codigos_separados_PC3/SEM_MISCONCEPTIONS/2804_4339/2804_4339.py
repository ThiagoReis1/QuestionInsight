depo= float(input("Deposito inicial:"))
meses= int (input("Quantos meses?:"))
i=0
while(meses > i):
	depo= depo + (depo*0.01)
	i= i + 1
	print(round(depo,2))