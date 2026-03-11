ano = int(input("Ano de nascimento : "))
pais = input("Brasil (B) ou Estados Unidos(E) : ").upper()

idade = 2023 - ano

if pais == "B" :
	if idade >= 18 :
		print("sim")
		print(idade - 18)
	else :
		print("nao")
		print(18 - idade)
elif pais == "E" :
	if idade >= 16 :
		print("sim")
		print(idade - 16)
	else :
		print("nao")
		print(16 - idade)
else :
	print("invalido")