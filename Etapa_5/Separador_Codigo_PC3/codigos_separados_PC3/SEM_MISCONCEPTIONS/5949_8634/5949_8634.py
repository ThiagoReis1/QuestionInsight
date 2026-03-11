comi = input("B para bolo, C para croissant: ")
qnt_comi = int(input("Quantidade: "))
qnt_cap = int(input("Quantidade de cappuccinos: "))

if comi == "B":
	total = qnt_comi*3.0 + qnt_cap*5.5
	print(round(total, 2))
else:
	total = qnt_comi*6.0 + qnt_cap*5.5
	print(round(total, 2))