p = float(input("Preco do produto: "))
cod = int(input("Codigo do produto: "))

if (cod == 1):
	v = (p - p*0.40) + p * (10/100)
	print(v)
elif (cod == 2):
	v = (p - p*0.40) + p * (8/100)
	print(v)
elif (cod == 3):
	v = (p - p*0.40) + p * (0/100)
	print(v)
elif (cod == 4):
	v = (p - p * 0.40) + p * (2/100)
	print(v)
	