entrada = input("aminoacido").upper()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
alanina = (c * 3) + (h * 7) + (n) + (o * 2)
valina = (c * 5) + (h * 11 ) + (n) + (o * 2)
tirosina = (c * 9) + (h * 11) + (n) + (o * 3)

if( entrada == "alanina"):
	print(round(alanina, 2))
elif( entrada == "valina"):
	print(round(valina, 2))
elif( entrada == "tirosina"):
	print(round(tirosina, 2))
else:
	print("Entrada:", a)
	print("Dado Invalido")
	