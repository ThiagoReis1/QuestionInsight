resul = input("").upper()

contador = 0

while resul != 'X':
	if resul == 'A':
		contador = contador + 1
	resul = input("").upper()
print(contador)