string = input("string: ")

if len(string) >= 2:
	if string[1].lower() == 's':
		print(string.upper())
	else:
		print("nome invalido")
else:
	print("nome invalido")
	
