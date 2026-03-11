n = int(input("insira o numero referente ao ano de nascimento: "))
p = input("insira o pais que deseja verifar a idade: (B/R) ").upper()
idade = 2023 - n
if p == "B":
	if idade >= 21:
		print("sim")
		print(idade - 21)
	else:
		print("nao")
		print(21 - idade)
elif p == "R":
	if idade >= 18:
		print("sim")
		print(idade - 18)
	else:
		print("nao")
		print(18 - idade)
else:
	print("invalido")
	
	
		
		
		
	
	
	
	
		  