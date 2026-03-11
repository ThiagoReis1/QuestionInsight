item = input("L/P")
quantidade = int(input("quantidade"))
refrigerante = int(input("refrigerante")
lan = 6.0
prat = 13.5
refrigerante = 3.0
if item.upper() == "L":
	total = 6 * quantidade + refrigerante * 3
	print(round(total,  2))
else:
	total = 13.5 * quantidade + refrigerante * 3
	print(round(total,  2))