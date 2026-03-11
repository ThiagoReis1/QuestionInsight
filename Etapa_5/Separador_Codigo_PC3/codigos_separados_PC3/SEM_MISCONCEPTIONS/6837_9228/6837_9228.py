s = input("").upper()

i = 0
valor = 0
while i < len(s):
	if s[i] == "I":
		valor = valor + 3.75
	elif s[i] == "M":
		valor = valor + 4.5
	else:
		valor = valor + 2.9
	i = i + 1
print(round(valor, 2))