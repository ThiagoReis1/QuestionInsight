adn = int(input("data de nascimento: "))
idade_dirigir = input("qual o pais (B/R): ")

idade = 2023 - adn

if idade_dirigir == "B":
	if idade >= 18:
		print("sim")
		print(idade - 18)
	else:
		print("nao")
		print(18 - idade)
elif idade_dirigir == "R":
	if idade >= 17:
		print("sim")
		print(idade - 17)
	else: 
		print("nao")
		print(17 - idade)
else:
	print("invalido")
	
	
	
	
	