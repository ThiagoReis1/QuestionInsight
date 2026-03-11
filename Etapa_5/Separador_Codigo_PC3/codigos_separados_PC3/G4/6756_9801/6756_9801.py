NDR = int(input("Numero de dias reservados: "))
D = 175

if NDR < 15:
	print(round(D * NDR + 20, 2))
elif NDR == 15:
	print(round(D * 15 + 16, 2))
else:
	print(round(D * NDR + 10, 2))