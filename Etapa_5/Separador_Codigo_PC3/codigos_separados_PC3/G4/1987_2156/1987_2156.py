ami = input("aminoacido desejado: ").upper()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794

if (ami == "ALANINA"):
	pm = ((c*3) + (h * 7) + n + (o * 2))
	print(round(pm, 2))
elif (ami == "VALINA"):
	pm = ((c * 5) + (h * 11) + n + (o * 2))
	print(round(pm, 2))
elif (ami == "TIROSINA"):
	pm = ((c * 9) + (h * 11) + n + (o * 3))
	print(round(pm, 2))
else:
	print("Entrada: ", ami)
	print("Dado Invalido")