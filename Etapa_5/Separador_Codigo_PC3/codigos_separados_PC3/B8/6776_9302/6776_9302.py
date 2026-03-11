ano = int(input("idade: "))
pais = input("pais: ")

if pais not in ("B,R"):
	print("invalido")
	
if 2023 - ano < 18 and pais == 'B':
	print('sim')
	conta = 18 - (2023 - ano)
	print(conta)
	
else:
	if 2023 - ano >= 17 and pais == 'R':
		print('sim')
		conta = (2023 - ano) - 17
		print(conta)
	else:
		if 2023 - ano < 17 and pais == 'R':
			print('nao')
			conta = 17 - (2023 - ano)
			print(conta)
			
		else:
			if 2023 - ano >= 18 and pais == 'B':
				print('sim')
				conta = (2023 - ano) - 18
				print(conta)
			
		
		

	
	