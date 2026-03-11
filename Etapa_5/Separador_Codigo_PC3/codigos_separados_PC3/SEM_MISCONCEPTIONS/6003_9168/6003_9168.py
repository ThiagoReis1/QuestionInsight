cen = float(input("Quantas cenouras foram compradas? "))

if cen < 5:
	total = (1.2*cen)
	print(round(total, 2))
if cen >= 5:
	valor = (0.9*cen)
	print(round(valor, 2))