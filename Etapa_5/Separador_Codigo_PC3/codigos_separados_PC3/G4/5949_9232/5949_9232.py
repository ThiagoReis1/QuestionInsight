bouc = input("b ou c: ")
quantidade = int(input("quantos? "))
capp = int(input("quantos capp? "))

B = 3.00
C = 6.00
C2 = 5.50

if (bouc.upper() == "B"):
	print(round(((B * quantidade) + (C2 * capp)), 1))

else:
	print(round(((C * quantidade) + (C2 * capp)), 1))