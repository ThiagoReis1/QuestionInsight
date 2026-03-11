amino = input("Nome do Aminoácido:")

O = 15.9994
C = 12.0110
N = 14.0067
H = 1.00794

if amino.upper() == "GLUTAMINA":
	glutamina = (C*5) + (H*8)+ N + (O*4)
	print (round(glutamina,2))
if amino.upper() == "TREONINA":
	treonina = (C*4) + (H*9) + N + (O*3)
	print (round(treonina,2))