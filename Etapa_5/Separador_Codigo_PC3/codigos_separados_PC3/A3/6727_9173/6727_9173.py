x = int(input(" Digite o valor x: "))


resto = x%31
quociente = x//31

if resto == 0:
	print(x//31)
	print("sim")
else:
	print(resto)
	print("nao")