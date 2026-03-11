area = int(input("Quantos hectares: "))


if(area <= 10000):
	preco = 5 * area
	
else:
	x = area - 10000
	preco = 5 * 10000 + 4 * x
	
print(preco)
