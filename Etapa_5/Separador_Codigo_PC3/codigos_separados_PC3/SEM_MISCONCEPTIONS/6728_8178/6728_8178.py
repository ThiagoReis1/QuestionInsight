X = int(input("numero para teste: "))

if X % 37 == 0:
	quociente = X // 37
	print(quociente)
	print("sim")
else:
	resto = X % 37
	print(resto)
	print("nao")
	