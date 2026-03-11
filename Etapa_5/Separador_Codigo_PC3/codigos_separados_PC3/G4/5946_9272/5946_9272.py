loup = input("digite \"L\" para lanche ou \"P\"para pizza:")
qlp = int(input("quantidade de lanches ou pizza:"))
qr = int(input("quantidade de refrigerantes"))
if loup == "L":
	x = qlp * 6.00 + qr * 3.00
	print(round(x,2))
else:
	y = qlp * 4.50 + qr * 3.00
	print(round(y,2))