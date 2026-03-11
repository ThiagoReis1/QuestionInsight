consumo= int(input())

if(consumo<=100):
	consumo = consumo* 1.20
	
	print(round(consumo,2))
	
else:
	consumo = 25 + 1.40*(consumo)
	print(round(consumo,2))
	
	

	