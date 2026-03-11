x = int(input("digite o numero: "))

if (x%41==0):
	calculo = x//41
	print(calculo)
	print("sim")
else: 
	calculo = x%41
	print(calculo)
	print("nao")