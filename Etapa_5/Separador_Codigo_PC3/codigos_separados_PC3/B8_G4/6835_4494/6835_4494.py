bisc = 3.75
cere = 7.9
enla = 9.85

string = input()
cont = 0
soma = 0

while cont < len(string):
	if string[cont].upper() == "B":
		soma += bisc
	elif string[cont].upper() == "C":
		soma += cere
	elif string[cont].upper() == "E":
		soma += enla
	cont += 1

print(round(soma, 2))