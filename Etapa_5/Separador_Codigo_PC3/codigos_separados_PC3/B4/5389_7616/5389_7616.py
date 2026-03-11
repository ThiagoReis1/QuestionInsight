from numpy import*
senha = input("Senha: ").upper()

i = 0

v = 0


while i < len(senha):
#	print(senha[i])
	if senha[i] == "A":
		v = v + 3.15
	elif senha[i] == "E":
		v = v + 3.15
	elif senha[i] == "I":
		v = v + 3.15
	elif senha[i] == "O":
		v = v + 3.15
	elif senha[i] == "U":
		v = v + 3.15
	else:
		v = v + 4.17
	i = i +1
print(round(v, 2))