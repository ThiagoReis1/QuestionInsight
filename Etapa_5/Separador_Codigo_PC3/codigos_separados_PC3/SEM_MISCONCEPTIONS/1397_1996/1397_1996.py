#Prova 02 - Ex 01

area = float(input("Qual a area a ser fertilizada (em hectares)? "))

if (area <= 10000):
	custo = 5 * area
	print(round(custo,2))
	
else:
	custo = (5 * (area - (area - 10000))) + (4) * (area - 10000)
	print(round(custo,2))
	