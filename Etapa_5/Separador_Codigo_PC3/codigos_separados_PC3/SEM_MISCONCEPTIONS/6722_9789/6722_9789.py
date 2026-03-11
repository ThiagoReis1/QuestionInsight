num = int(input("digite um numero inteiro: "))
if num % 17 == 0:
	quoficiente = num // 17
	print(quoficiente)
	print("sim")
else:
	resto = num % 17
	print(resto)
	print("nao")
  