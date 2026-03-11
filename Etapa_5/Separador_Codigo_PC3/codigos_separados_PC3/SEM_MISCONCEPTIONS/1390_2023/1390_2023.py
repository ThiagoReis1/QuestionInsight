# Plano de telefonia.

consumo = int(input("digite o consumo:"))

if(consumo<=100):
	valor = (consumo*1.20)
	
else:
	valor =(25+(consumo*1.40))
	
print(round(valor,2))