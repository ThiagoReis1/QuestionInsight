from numpy import*
palavra = input("Digite a palavra: ").upper()
i=0
j=0
while i < len(palavra):
	if palavra[i] == "A":
		j = j + 1.12
	elif palavra[i] == "E":
		j = j + 1.12
	elif palavra [i] == "I":
		j = j + 1.12
	elif palavra[i] == "O":
		j = j + 1.12
	elif palavra[i] == "U":
		j = j + 1.12
	else:
		j = j + 1.18
	i  = i + 1
print(round(j, 2))
	  