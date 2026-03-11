string = input("nome: ")

letra1 = string[0]

if letra1.lower() == "m":
	N = string.upper()
	print(N)
else:
	print("nome invalido")