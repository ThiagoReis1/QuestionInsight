a = input("unidade:")
b = float(input("medida: "))

if a == "M":
	g = 1.60934 * b
	print(round(g,2))
elif a == "K":
	h = b/1.60934
	print(round(h,2))