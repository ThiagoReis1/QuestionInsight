am =  input("Nome do aminoacido: ")

arginina = (12.011*6) + (1.00794*15) + (4*14.00674) + (2*15.9994)
tirosina = (12.011*9) + (1.00794*11) + (14.00674) + (3*15.9994)

if (am == "arginina".upper()):
	print(round(arginina, 2))
else:
	print(round(tirosina, 2))