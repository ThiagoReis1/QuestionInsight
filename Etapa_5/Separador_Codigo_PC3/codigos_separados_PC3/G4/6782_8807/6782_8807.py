n = int(input("Nascimento: "))
p = input("Pais: ").upper()
ano_atual = 2023
if p == "B" and (ano_atual - n) >= 18:
	t = (ano_atual - n) - 18
	print("sim")
	print(t)
elif p == "B" and (ano_atual - n) < 18:
	t = (- ano_atual + n) + 18
	print("nao")
	print(t)
elif p == "E" and (ano_atual - n) >= 16:
	t = (ano_atual - n) - 16
	print("sim")
	print(t)
elif p == "E" and (ano_atual - n) < 16:
	t = (- ano_atual + n) + 16
	print("nao")
	print(t)
else:
	print("invalido")