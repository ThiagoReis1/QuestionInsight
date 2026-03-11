tos = input("T ou S: ")
qnt = int(input("quantidade: "))
acai = int(input("quantidade: "))

if (tos.upper() == "T"):
	total = qnt * 5.50 + acai * 10.00
	print(round(total, 2))
else:
	total = qnt * 4.00 + acai * 10.00
	print(round(total, 2))