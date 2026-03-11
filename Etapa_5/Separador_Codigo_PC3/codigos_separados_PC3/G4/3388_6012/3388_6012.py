m = input("medida: ")
v = float(input("value: "))
if(m == "B"):
	w = v / 3.41214
	print(round(w, 2))
else: 
	b = 3.41214 * v
	print(round(b, 2))