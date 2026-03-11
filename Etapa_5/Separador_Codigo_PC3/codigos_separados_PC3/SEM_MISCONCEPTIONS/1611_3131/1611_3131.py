etiq = input("etiqueta: ").upper()
vogal = 0.15
outro = 0.17

i = 0
cont = 0
cont2 = 0

while (i < len(etiq)):
	if (etiq[i] == "A" or etiq[i] == "E" or etiq[i] == "I" or etiq[i] == "O" or etiq[i] == "U"):
		cont = cont + 1
		i = i + 1
	else:
		cont2 = cont2 + 1
		i = i + 1

total = (cont * vogal) + (cont2 * outro)
print(total)