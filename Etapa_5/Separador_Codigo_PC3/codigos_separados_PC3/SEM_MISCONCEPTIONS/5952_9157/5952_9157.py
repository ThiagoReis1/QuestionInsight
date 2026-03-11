conta = input("T/S").upper()
qtd_c = int(input("quantidade de comida: "))
qtd_a = int(input("quantidade de acai: "))
if conta == "T":
	total = qtd_c*3.5+13*qtd_a
	print(round(total, 2))
else :
	total = qtd_c*5.+13*qtd_a
	print(round(total, 2))