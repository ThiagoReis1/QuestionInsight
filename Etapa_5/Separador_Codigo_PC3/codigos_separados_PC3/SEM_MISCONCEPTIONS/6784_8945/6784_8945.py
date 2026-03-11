ano_nasc = int(input("Digite o ano de nascimento: "))
pais = input("Digite: ").upper()

ano_consulta = 2023

if pais == "B":
	idade_minima = 21
elif pais == "R":
	idade_minima = 18
else:
	print("invalido")
	
idade = ano_consulta - ano_nasc	
	
if idade >= idade_minima:
	print("sim")
	print(idade - idade_minima)
else:
	print("nao")
	print(idade_minima - idade)
	