x = int(input("X: "))
quociente = x//37
resto = x%37

if resto == 0:
	print(quociente)
	print("sim")
else:
	print(resto)
	print("nao")