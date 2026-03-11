palavra = str(input())
palavra = palavra.upper()
valor = 0
for i in palavra:
	if i in "AEIOU":
		valor = valor + 45.15
	else:
		valor = valor + 50.17

print(round(valor, 2))