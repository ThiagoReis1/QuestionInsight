X = int(input("x: "))
quociente = X//19
resto = X%19

if resto == 0:
	print(quociente)
	print("sim")
else:
	print(resto)
	print("nao")