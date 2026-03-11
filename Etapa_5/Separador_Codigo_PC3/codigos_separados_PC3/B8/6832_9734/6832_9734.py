itens = input("itens")
H = 5.40
C = 8.95
L = 4.50

total = 0

for itens in itens:
	if itens == "H":
		total += H
	elif itens == "C":
		total += C
	elif itens == "L":
		total += L
print(round(total, 2))