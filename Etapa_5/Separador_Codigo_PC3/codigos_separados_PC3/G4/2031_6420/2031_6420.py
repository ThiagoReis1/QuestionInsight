r = int(input("Resultado do lancamento:"))
acu = 0

while (r != -1) and (r == 1) or (r == 2) or (r == 3) or (r == 4) or (r == 5) or (r == 6):
		if (r == 6):
			acu = acu + 1
		r = int(input("Resultado do lancamento:"))
print(acu)