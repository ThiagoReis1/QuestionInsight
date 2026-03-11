valor = float(input("total da compra: "))
codigo = input("opcao: ").upper()

if codigo == "C":
	x = int(input("de quantas vezes voce quer: "))
	if x == 2:
		t = valor + (valor * (9/100))
		print(round(t, 2))
	else:
		t = valor 
		print(t)
elif codigo == "P":
	f = valor - (valor * 0.19)
	print(round(f, 2))
elif codigo == "D":
	f = valor -  (valor * 0.19)
	print(round(f, 2))