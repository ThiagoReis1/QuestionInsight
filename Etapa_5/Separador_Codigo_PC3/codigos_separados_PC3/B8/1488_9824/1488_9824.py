minutos = int(input("insira os minutos: "))
 

if minutos >= 0 and minutos <= 100:
		valor = minutos * 1.20 + 1.00
		
elif minutos > 100 and minutos <= 200:
	valor = minutos * 1.30 + 10.00
		
elif minutos > 200 and minutos <= 300:
	valor = minutos * 1.40 + 20.00
		
elif minutos > 300:
	valor = minutos * 1.50 + 25.00
	
print(round(valor, 2))