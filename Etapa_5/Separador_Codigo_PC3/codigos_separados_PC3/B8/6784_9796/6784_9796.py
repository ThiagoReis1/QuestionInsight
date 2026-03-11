ano_nasc = int(input("Digite o ano de nascimento"))
pais = input("B para Brasil e R para Reino Unido")

idade = 2023 - ano_nasc

if idade >= 21 and pais == 'B' or pais == 'b':
	print("sim")
	print(idade-21)
elif idade < 21 and pais == 'B' or pais == 'b':
	print("nao")
	print(21-idade)
elif idade >= 18 and pais == 'R' or pais == 'r':
	print("sim")
	print(idade - 18)
elif idade < 18 and pais == 'R' or pais =='r':
	print("nao")
	print(18 - idade)
elif pais != 'B' and pais != 'R':
	print("invalido")
