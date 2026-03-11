l = input()
lanche_or_salgado = int(input())
refri = int(input())
if l == "L":
	x = 5*lanche_or_salgado + 4*refri
	print(round(x,2))
else:
	x = 3.50*lanche_or_salgado + 4*refri
	print(round(x,2))
	