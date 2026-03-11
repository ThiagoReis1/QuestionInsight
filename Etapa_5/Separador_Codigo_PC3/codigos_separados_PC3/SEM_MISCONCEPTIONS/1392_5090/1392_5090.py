consumo = float(input("consumo de  agua: "))

# Condicoes 

if (consumo < 10):
	valor = 30 + consumo*3
	print(round(valor,2))
	
else:
	valor = 30 + consumo *3.5
	print(round(valor,2))