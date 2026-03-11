senha = input("Senha: ").upper()
i = 0
t = 0
while i < len(senha):
	if senha[i] == "A":
		t = t + 1.12
	elif senha[i] == "E":
		t = t + 1.12
	elif senha[i] == "I":
		t = t + 1.12
	elif senha[i] == "O":
		t = t + 1.12
	elif senha[i] == "U":
		t = t + 1.12
	else:
		t = t + 1.18
	i = i + 1
print(round(t ,2))