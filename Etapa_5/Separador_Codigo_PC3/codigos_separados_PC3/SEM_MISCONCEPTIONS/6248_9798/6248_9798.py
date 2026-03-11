b = input("P/C/A: ").upper()
contador = 0
while b != X:
	if b == "A":
		contador = contador + 1
	b = input("P/C/A: ").upper()
print(contador)