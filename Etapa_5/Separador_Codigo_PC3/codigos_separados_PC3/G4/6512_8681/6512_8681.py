a = int(input("Insira a quantidade de Duplas Deliciosas: "))

if (a > 3):
	b = (a*32.90)*(20/100)
	c = (a*32.90) - b
else:
	c = a*32.90
	
print(round(c,2))