ano_nasc = int(input("ano: "))
pais = input("B ou R: ")

brasil = 18
russia = 21


ano_pesquisa = 2023

idade = ano_pesquisa - ano_nasc
anos_apta = idade - 18
anos_2apta = idade - 21
anos_3apta = 18 - idade
anos_4apta = 21 - idade

if(pais == "B" and idade >= brasil) or (pais == "R" and idade >= russia):
	print("sim")
	print(anos_apta)
	
else:
	print("nao")
	print(anos_2apta)