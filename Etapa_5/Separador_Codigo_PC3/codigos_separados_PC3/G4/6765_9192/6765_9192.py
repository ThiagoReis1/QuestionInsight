An = int(input("Informe o ano de nascimento: "))
Pv = input("Informe o pais que deseja verificar(\"B\" para Brasil e \"R\" para Russia): ").upper()
Cl = 2023 - An
Ib = 18 - Cl
Ir = 21 - Cl

if Pv == "B":
	if Cl >= 18:
		print("sim")
		print(Ib)
	else:
		print("nao")
		print(Ib)
		
elif Pv == "R":
	
	if Cl >= 21:
		print("sim")
		print(Ir)
	else:
		print("nao")
		print(Ir)
		
else:
	print("invalido")
