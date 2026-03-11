peso= float(input("peso: "))

if (peso<5000):
	valor= (0.05*peso)
	print(round(valor,2))

else:
	valor= (0.04*peso)+ 60
	print(round(valor, 2))
