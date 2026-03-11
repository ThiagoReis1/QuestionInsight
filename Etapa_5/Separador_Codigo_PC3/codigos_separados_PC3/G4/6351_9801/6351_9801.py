v = input("Nome? ").upper()

if v[-1] != "S":
	print("nome invalido")
else:
	i = 0
	while i < len(v):
		if v[-1] == "S":
			i = i + 1
	print(v)