m=input("digite a unidade (M/K)")
kl=float(input("digite o valor da medida"))

if (m.upper()=="K"):
	x=2.35215*kl
	
else: 
	x=kl/2.35215
	
print(round(x,2))
	