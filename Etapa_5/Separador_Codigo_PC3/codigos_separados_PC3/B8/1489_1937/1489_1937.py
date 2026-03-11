energia = float(input())


if(0 <= energia and energia <= 150):
	valor = (energia*0.6) + 5
	print(round(valor,2))

elif(150 < energia and energia <= 250):
	valor = (energia*0.65) + 8
	print(round(valor,2))

elif(250 < energia and energia <= 350):
	valor = (energia*0.7) + 12
	print(round(valor,2))
	
elif(energia > 350):
	valor = (energia*0.75) + 16
	print(round(valor,2))
	
	
	
	
