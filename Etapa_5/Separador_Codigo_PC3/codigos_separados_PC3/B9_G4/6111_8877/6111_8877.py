com = float(input("Informe a quantidade de combustivel no tanque: "))

if com < 17.5:
	print(round(com + 10.5, 1))
elif com >= 17.5 and com < 35:
	print(round(com + 14, 1))
elif com >= 35 and com < 50:
	print(round(com + 18,6, 1))
else:
	print(round(com + 24.5, 1))