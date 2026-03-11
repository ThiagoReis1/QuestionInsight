n = input("Qual o nome do aminoácido? ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794

psAl = (C * 3) + (H * 7) + (N * 1) + (O * 2)

psVa = (C * 5) + (H * 11) * (N * 1) + (O * 2)

if (n == "alanina".upper()):
	print(round(psAl,2))

else:
	print(round(psVa,2))		
			





