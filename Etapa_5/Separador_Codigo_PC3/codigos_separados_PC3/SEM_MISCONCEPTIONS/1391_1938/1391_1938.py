consumo = float(input("quanto consumiu: "))
a = 5 + 0.6 * consumo
b = 16 + 0.75 * consumo
if(consumo <= 150):
	print(a)
else:
	print(b)