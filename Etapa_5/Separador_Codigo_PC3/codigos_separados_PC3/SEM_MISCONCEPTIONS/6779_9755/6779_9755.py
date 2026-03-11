ano = int(input("digite o ano de nascimento: "))
pais = input("digite B ou J: ").upper()

if pais == 'B':
	idade = (2023 - ano)
	
	if idade >= 18:
		resto = (idade - 18)
		print("sim")
		print(resto)
		
	else:
		falta = (18 - idade)
		print("nao")
		print(falta)
		
elif pais == 'J':
	idade = (2023 - ano)
	
	if idade >= 16:
		resto = (idade - 16)
		print("sim")
		print(resto)
		
	else: 
		falta = (16 - idade)
		print("nao")
		print(falta)
		
else:
	print("invalido")