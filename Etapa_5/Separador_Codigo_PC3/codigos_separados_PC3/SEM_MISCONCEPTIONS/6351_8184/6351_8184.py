string = input("ultima letra do nome: ").lower()
if (string[-1] == "s"):
	print(string.upper())
else:
	print("nome invalido")