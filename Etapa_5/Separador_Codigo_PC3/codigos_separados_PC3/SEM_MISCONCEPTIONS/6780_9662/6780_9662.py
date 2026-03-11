ano = int(input("ano de nascimento:"))
pais = input("pais:").upper()
if pais=="B":
	idade = 2023-ano
	if idade>=21:
		print("sim")
		apta = (idade-21)
		print(apta)
	else:
		print("nao")
		falta = (21-idade)
		print(falta)
elif pais=="C":
	idade = 2023-ano
	if idade>=24:
		print("sim")
		apta = (idade-24)
		print(apta)
	else:
		print("nao")
		falta = (24-idade)
		print(falta)
else:
	print("invalido")
		
	
	
