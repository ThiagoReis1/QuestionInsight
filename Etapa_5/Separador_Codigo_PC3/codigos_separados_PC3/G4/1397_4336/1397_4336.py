hec = int(input("Quantos hectares serao fertilizados? "))

if (hec <= 10000):
	print(round(hec * 5 , 2))
else:
	print(round(10000 * 5 + (hec - 10000) * 4 , 2))
