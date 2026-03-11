e = input("etiqueta: ").upper()
vogal = 0.15
outro = 0.17

i = 0
cont = 0
cont2 = 0

while (i < len(e)):
	if (e[i] == "A" or e[i] == "E" or e[i] == "I" or e[i] == "O" or e[i] == "U"):
		cont = cont + 1
		i = i + 1
	else:
		cont2 = cont2 + 1
		i= i + 1
		
total = (cont * vogal) + (cont2 * outro)
print(total)
		