a = int(input("ano de nascimento: "))
p = input("Pais:").upper()
i = 2023 - a
if p == "B" and i >= 21:
	q = i - 21
	print("sim", q)
elif p == "B" and i < 21:
	q = 21 - i
	print("nao", q)
elif p == "R" and i >= 18:
	q = i - 18
	print("sim", q)
elif p == "R" and i < 18:
	q = 18 -i
	print("nao")

else:
	print("invalido")

	