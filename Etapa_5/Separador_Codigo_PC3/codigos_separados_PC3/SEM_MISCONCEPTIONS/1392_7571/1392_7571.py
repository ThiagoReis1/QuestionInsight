consumo= float(input("digite o consumo: "))
if(consumo==0):
	valor= consumo+30
	print(round(valor,2))
if(consumo<10):
	valor=(consumo*3)+30
	print(round(valor,2))
if(consumo>10):
	valor=(consumo*3.5)+30
	print(round(valor,2))