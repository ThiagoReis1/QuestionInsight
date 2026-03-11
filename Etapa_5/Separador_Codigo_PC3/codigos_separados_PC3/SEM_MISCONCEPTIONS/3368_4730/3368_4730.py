escala=input("C ou K")
valor=float(input("valor da temperatura"))

if(escala.upper()=="C"):
	resultado =valor+273.15
	
else:
	resultado= valor -273.15
print(round(resultado,2))