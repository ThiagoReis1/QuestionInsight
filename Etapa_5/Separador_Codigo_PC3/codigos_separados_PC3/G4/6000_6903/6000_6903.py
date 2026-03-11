nc = int(input("Insira o numero de cachos: "))

if nc < 3:
	t = nc*5
	print(round(t,2))
else:
	t = nc*4.25
	print(round(t,2))