quantidade = int(input("qual a quantidade de frutas compradas: "))

if quantidade < 6:
	t = quantidade * 3.80
	print(round(t, 2))
else:
	t = quantidade * 3.45
	print(round(t, 2))
	