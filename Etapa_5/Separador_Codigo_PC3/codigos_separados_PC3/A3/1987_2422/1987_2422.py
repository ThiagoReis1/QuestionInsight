val = input("aminoacido: ").lower()

O = 15.99
C = 12.01
N = 14.00
H = 1.00

alanina = (c*3) + (h*7) + (n) + (o*2)
valina = (c*5) + (h*11) + (n) + (o*2)
tirosina = (c*9) + (h*11) + (n) + (o*3)
if (val == "alanina"):
	print(round(glutamina,2))
elif (val == "valina"):
	print(round(valina,2))
elif (val == "tirosina"):
	print(round(tirosina, 2))
else:
		print("Entrada:", val)
		print("Dado Invalido")