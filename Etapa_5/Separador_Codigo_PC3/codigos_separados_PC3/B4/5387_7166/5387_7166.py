from numpy import*
palavra = input("digite a palavra: ").upper()
i = 0
j = 0

while i < len(palavra):
	if palavra[i] == "A":
		j = j + 45.12
	elif palavra[i] == "E":
		j = j + 45.12
	elif palavra[i] == "I":
		j = j + 45.12
	elif palavra[i] == "O":
		j = j + 45.12
	elif palavra[i] == "U":
		j = j + 45.12
	else:
		j = j + 50.18
	i = i + 1
print(round(j, 2))
	