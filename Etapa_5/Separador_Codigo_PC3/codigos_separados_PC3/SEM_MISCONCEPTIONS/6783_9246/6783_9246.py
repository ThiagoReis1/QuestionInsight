ano_nascimento = int(input("digite ano "))
pais = input("digite ( B para Brasil, E para Estados Unidos ): ")

idade_brasil = 18
idade_eua = 16
ano_consulta = 2023

ano_consulta = ano_consulta - ano_nascimento 

if (pais == "B" and idade >= idade_brasil) or (pais == "E" and idade >= idade_eua):
	print("sim")
else:
	print("nao")
else: 
	print("invalido")




