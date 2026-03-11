#TORTA OU PASTEL
a = input("digite T ou P: ")

#QUANTIDADE DE TORTA OU PASTEL
b = int(input("digite a quantidade: "))

#QUANTIDADE DE DE CAPPUCCINOS
c = int(input("digite a quantidade: "))

d = (b * 6) + (c * 4.50)
e = (b * 5) + (c * 4.50)

if (a == "T"):
	d = (b * 6) + (c * 4.50)
	print(round(d,1))
else:
	e = (b * 5) + (c * 4.50)
	print(round(e,1))