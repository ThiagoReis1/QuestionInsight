a = input("aminoacido: ").upper()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
arginina = (c*6) + (h*15) + (n*4) + (o*2)
tirosina = (c*9) + (h*11) + (n) + (o*3)
triptofano = (c*11) + (h*11) + (n*2) + (o*2)
if (a == "ARGININA"):
	print(round(arginina, 2))
elif (a == "TIROSINA"):
    print(round(tirosina, 2))
elif (a == "TRIPTOFANO"):
    print(round(triptofano, 2))
else:
	print("Entrada:",a)
	print("Dado Invalido")
