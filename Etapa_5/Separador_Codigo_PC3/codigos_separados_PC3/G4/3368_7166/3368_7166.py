temp = input("Temperatura em (C/K): ")

if(temp == "C"):
	c =  float(input("digite em Celsius: "))
	K = c + 273.15
	print(round(K, 2))
else:
	k = float(input("Digite em Kelvin"))
	C = k - 273.15
	print(round(C, 2))
	