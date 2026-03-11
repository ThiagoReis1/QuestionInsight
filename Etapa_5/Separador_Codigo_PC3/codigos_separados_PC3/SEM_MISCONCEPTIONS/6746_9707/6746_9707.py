codigo = int(input("digite o codigo da sorte: "))

if codigo == 21:
	print("sorte")
else:
	if codigo < 21:
		print("menor")
	else:
		print("maior")