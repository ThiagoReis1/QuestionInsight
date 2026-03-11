from numpy import*

v = input("etiqueta: ").upper()

i = 0
preco = 0

while(i < len(v)):
	if(v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U"):
		preco = preco  + 0.15
	else:
		preco = preco + 0.17
	
	i = i + 1

print(round(preco, 2))
		