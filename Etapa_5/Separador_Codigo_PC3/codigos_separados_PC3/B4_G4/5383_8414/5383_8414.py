x = input("").upper()
cont = 0

for i in x:
	if i == "A":
		cont = cont * 0.12
	elif i == "E":
		cont = cont * 0.12
	elif i == "I":
		cont = cont * 0.12
	elif i == "O":
		cont = cont * 0.12
	elif i == "U":
		cont = cont * 0.12
	else:
		cont = cont * 0.18

print(round(cont, 2))