valor = float(input("digite um valor: "))
codigo = input().upper()

if codigo == "D" or codigo == "P":
	total = valor - (valor * 0.13)
	print(round(total, 2))
elif codigo == "C":
	vezes = int(input("digite: "))
	if vezes == 1:
		print(round(valor, 2))
	elif vezes == 2:
		print(round(valor + (valor * 0.08),2))