x = int(input("Quantidade de aboboras:"))
s = 3.80*x
c = 3.45*x
if x >= 5:
	print(round(c, 2))
else:
	print(round(s, 2))