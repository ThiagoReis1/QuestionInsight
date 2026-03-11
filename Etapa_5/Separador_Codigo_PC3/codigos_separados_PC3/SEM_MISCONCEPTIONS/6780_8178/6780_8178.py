idade_minima_B = 21
idade_minima_C = 24
ano = 2023

ano_nasc = int(input("ano de nascimento: "))
pais = input("pais para consulta").upper()
idade = ano - ano_nasc

if (pais == "B" and idade >= idade_minima_B):
	print("sim")
	print(idade_minima_B - idade)
elif pais == "B" idade_minima_B < idade_minima_B:
	print("nao")

if (pais == "C" and idade >= idade_minima_C):
	print("sim")
	print(idade_minima_C - idade)
elif pais == "C"


if pais != "B" and pais != "C":
	print("invalido")