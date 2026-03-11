ano = int(input("Ano de nascimento:"))
pais = input("BR ou EUA:")

if (pais.upper() == 'E'):
	if (ano < 2006):
		print("sim")
		print(2005 - ano)
	
	else:
		print("nao")
		print(ano - 2005)
		
elif (pais.upper() == 'B'):
	if (ano < 2003):
		print("sim")
		print(2002 - ano)
		
	else:
		print("nao")
		print(ano - 2002)
		
else:
	print("invalido")