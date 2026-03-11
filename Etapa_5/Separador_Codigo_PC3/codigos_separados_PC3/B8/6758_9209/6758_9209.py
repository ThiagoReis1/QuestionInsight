dias = int(input("alugando por quantos dias: "))

if dias < 7:
	total = dias * 100.00 + 15.00
elif dias == 7:
	total = dias * 100.00 + 12.00
elif dias > 7:
	total = dias * 100.00 + 10.00
print(round(total,2))