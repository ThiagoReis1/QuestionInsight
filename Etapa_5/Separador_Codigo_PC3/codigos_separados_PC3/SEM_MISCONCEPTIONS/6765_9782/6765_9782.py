ano_nascimento = int(input("Digite o ano nascimento: "))
pais = input("(B) para Brasil e (R) para Russia: ").upper()
idade = 2023 - ano_nascimento

if pais == "B" and idade >= 18:
	print("sim")
	falta = idade - 18
	print(falta)
elif pais == "B" and idade <18:
	print("nao")
	falta = 18 - idade
	print(falta)
elif pais == "R" and idade >= 21:
	print("sim")
	falta = idade - 21
	print(falta)
elif pais == "R" and idade <21:
	print("nao")
	falta = 21 - idade
	print(falta)
else:
	print("invalido")
