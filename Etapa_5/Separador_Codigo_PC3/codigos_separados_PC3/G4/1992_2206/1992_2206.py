p = input("").lower()

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

if (p == "glutamina"):
	g = (C * 5) + (H * 8) + (N * 1) + (O * 4)
	print(round(g, 2))
elif (p == "histidina"):
	h = (C * 6) + (H * 10) + (N * 3) + (O * 2)
	print(round(h, 2))
elif (p == "prolina"):
	r = (C * 5) + (H * 10) + (N * 1) + (O * 2)
	print(round(r, 2))
else:
	print("Entrada: ",p)
	print("Dado Invalido")