quantidade = int(input("quantidade "))
if quantidade < 12:
	total = quantidade*0.30
	print(round(total, 2))
else:
	total = quantidade*0.25
	print(round(total, 2))
