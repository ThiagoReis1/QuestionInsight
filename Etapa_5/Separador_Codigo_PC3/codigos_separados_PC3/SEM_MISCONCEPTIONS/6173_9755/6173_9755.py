a = input("digite sua avaliacao: ").upper()

contador = 0

while a != 'S':
	if a == 'SIM':
		contador = contador +1
	a = input("digite sua avaliacao: ").upper()
print(contador)