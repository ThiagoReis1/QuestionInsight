x = float(input("digite o peso: "))

if x >= 0 and x <= 5000:
	valor = (x * 0.03) + 20
	#print(valor)
elif x >= 5001 and x <= 6000:
	valor = (x * 0.04) + 25
	#print(valor)
elif x >= 6001 and x <= 7000:
	valor = (x * 0.05) + 30
	#print(valor)
else:
	valor = (x * 0.06) + 35
print(valor)