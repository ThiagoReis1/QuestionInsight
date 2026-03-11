consumo = float(input(' qual foi consumo de energia?'))

if(consumo<150):
	valor = ((consumo*0.60)+5.00)
	print(round(valor,2))
elif((consumo>=150)and(consumo<250)):
	valor = ((consumo*0.65)+8.00)
	print(round(valor,2))
elif((consumo>=250)and(consumo<350)):
	valor = ((consumo*0.70)+12.00)
	print(round(valor,2))
elif(consumo>=350):
	valor = ((consumo*0.75)+16.00)
	print(round(valor,2))
 