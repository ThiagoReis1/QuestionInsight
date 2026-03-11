consumo = float(input("digite seu consumo em minutos: "))
Valor = 0 
if consumo > 0 and consumo <= 100: 
	Valor = consumo*1.20 + 1
	
elif  consumo > 100 and consumo <=200:
	Valor = consumo*1.30 + 10
	
elif  consumo > 200 and consumo <= 300:
	Valor = consumo*1.40 + 20
	
elif consumo > 300: 
	Valor = consumo*1.50 + 25
 	

print(round(Valor, 2))
	 

	
 
	