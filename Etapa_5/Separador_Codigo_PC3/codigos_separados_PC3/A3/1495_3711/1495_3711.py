area = int(input("area da plantacao: "))

if (area >= 0 and area <= 10000):
	valor = area*6.00 + 100

if (area > 10000 and area <= 20000):
	valor = area*5.50 + 150

if (area > 20000  and area <= 30000):
	valor = area*5.00 + 200
	
if (area > 30000):
	valor = area*4.50 + 250
print(round(valor,2))