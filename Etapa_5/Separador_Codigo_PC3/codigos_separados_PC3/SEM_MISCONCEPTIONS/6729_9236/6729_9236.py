nmr = int(input("digite um numero:"))

if nmr % 41 == 0:
	quociente = nmr // 41
	print (quociente)
	print("sim")

else:
	resto = nmr % 41
	print(resto)
	print("nao")