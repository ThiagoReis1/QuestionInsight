x = int(input("Numero inteiro x: "))

if x % 43 == 0:
	quoc = (x // 43)
	print(quoc)
	print("sim")
	
else:
	rest = (x % 43)
	print(rest)
	print("nao")