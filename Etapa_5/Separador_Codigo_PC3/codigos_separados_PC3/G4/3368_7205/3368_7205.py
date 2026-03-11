a = input("escala: ")
b= float(input("temperatura: "))

if (a == "K"):
	c= b-273.15
	print(round (c,2))
else:
	K= b+273.15
	print(round(K,2))