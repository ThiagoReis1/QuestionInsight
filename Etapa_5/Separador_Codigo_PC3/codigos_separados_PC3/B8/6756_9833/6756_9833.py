dias = float(input())

if dias < 15:
	total = (dias * 175) + 20
	print(round(total,2))
elif dias == 15:
	total = (dias * 175) + 16
	print(round(total,2))
elif dias > 15:
	total = (dias * 175) + 10
	print(round(total,2))