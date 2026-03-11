a = int(input("digite o ano de nascimento:"))
p = input("digite o pais(B/C):").upper()

if p == "B":
	t = 2023 - a
	if t >= 21:
		print("sim")
		print(t - 21)
	else:
		print("nao")
		print(21 - (2023 - a))
		
elif p == "C":
	t = 2023 - a
	if t >= 24:
		print("sim")
		print(t - 24)
	else:
		print("nao")
		print( 24 - (2023 - a))
		
else:
	print("invalido")