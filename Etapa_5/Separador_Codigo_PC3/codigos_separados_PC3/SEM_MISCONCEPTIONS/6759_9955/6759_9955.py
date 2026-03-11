distancia=float(input(""))

if distancia==10:
	total=50+7.75
elif distancia>10:
	total=50+10.00
else:
	total=50+5.50
print(round(total, 2))
