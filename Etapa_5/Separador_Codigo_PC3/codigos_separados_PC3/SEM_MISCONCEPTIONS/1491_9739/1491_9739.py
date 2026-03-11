peso = float(input("informe o peso: "))

if 0 <= peso < 5000:
	valor = peso * 0.03 + 20
elif 5001 <= peso < 6000: 																																				
	valor = peso * 0.04 + 25
elif 6001 <= peso < 7000: 
	valor = peso * 0.05 + 30
else:
	valor = peso * 0.06 + 35
print(round(valor, 2))