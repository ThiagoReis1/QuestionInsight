v = input("Insira os itens: ").upper()

i = 0
valor = 0

while i < len(v):
	if v[i] == "A":
		valor += 16.75
	elif v[i] == "L":
		valor += 4.6
	elif v[i] == "P":
		valor += 2.85
	i += 1
		
print(round(valor, 2))