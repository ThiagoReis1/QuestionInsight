varl = float(input(" quantidade de cobustivel comum:"))
if (varl > 0) and (varl < 17.5):
	print(round(varl + 0.8,2))
if (varl > 17.5 ) and (varl < 35.0):
	print(round(varl + 1.3,2))
if (varl > 35.0) and ( varl < 50):
	print(round(varl + 2.1,2))
if (varl >= 50):
	print(round(varl + 3,2))


