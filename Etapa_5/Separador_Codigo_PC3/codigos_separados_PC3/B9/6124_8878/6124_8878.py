pt = float(input("gramas?: "))

if pt >= 3000 and pt <= 4500:
	if pt >= 4100:
		total = pt * 3
	elif pt >= 3900 and pt < 4100:
		total = pt * 2.1
	elif pt >= 3400 and pt < 3900:
		total = pt * 1.3

	else:
		total = pt * 0.8
	print(round(total, 1))
