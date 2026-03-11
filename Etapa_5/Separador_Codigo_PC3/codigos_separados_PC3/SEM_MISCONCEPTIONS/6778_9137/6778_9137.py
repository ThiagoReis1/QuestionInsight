nascimento = int(input("Ano de nascimento: "))
pais = input("Insira o pais, para o Brasil 'B' e para o Japao 'J': ").upper()

consulta = 2023

idade = consulta - nascimento

if (pais == 'B' and idade >= 21):
	print("sim")
	print(idade -21)
elif (pais == 'J' and idade >= 20):
	print("sim")
	print(20 - idade)
elif (pais == 'B' and idade < 21):
	print("nao")
	print(21 - idade)
elif (pais == 'J' and idade < 20):
	print("nao")
	print(20 - idade)
else:
	print("invalido")