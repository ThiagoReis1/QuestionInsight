x = int(input("Informe o valor de: "))

if(x % 37 == 0):
	q = x//37
	print(round(q, 0))
	print("sim")

else:
	resto = x % 37
	print(round(resto, 0))
	print("nao")
