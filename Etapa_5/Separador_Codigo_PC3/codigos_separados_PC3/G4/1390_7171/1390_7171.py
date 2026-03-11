#plano de telefonia

time= float(input("Digite o consumo em min:"))

tax1= 1.20
tax2= 1.40

if (time<=100):
	consumo= (time* tax1)
	
else:
	consumo= time*tax2 +25
	
print (round(consumo,2))
