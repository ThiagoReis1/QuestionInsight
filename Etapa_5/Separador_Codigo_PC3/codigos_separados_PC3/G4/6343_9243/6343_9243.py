nome = input("digite string:")

if len(nome) >= 2:

	if nome[1].lower() == 'a':
		print(nome.upper())
	else:
		print("nome invalido ")
	
else:
	print("nome invalido ")