ano_nascimento = int(input("Digite o ano de nascimento: "))
pais = input("Digite o pais ('B' para 'Brasil e 'E' para 'Estados Unidos): ").upper()

idade_minima_B = 21
idade_minima_E = 18

ano_consulta = 2023

idade = ano_consulta - ano_nascimento
	
if (pais == 'B' and idade >= 21):
	quantos_anos_apto = idade - 21
	print("sim")
	print(quantos_anos_apto)

elif (pais == 'B' and idade < 21):
	quantos_anos_faltam = 21 - idade
	print("nao")
	print(quantos_anos_faltam)

elif (pais == 'E' and idade >= 18):
	quantos_anos_apto = idade - 18
	print("sim")
	print(quantos_anos_apto)

elif (pais == 'E' and idade < 18):
	quantos_anos_faltam = 18 - idade
	print("nao")
	print(quantos_anos_faltam)
	
else:
	print("invalido")