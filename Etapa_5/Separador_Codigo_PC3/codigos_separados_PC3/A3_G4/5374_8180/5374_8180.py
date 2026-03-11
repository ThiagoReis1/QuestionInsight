from numpy import*
s = input(": ").upper()
cont = 0

for caractere in string:
	if caracter in "AEIOU":
		cont= cont * 0.15
	else:
		cont= cont * 0.17

print(round(cont, 2))