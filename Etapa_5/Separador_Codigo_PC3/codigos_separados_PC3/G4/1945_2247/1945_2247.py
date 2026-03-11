n = input("Nome do aminoacido: ")

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

x = (4 * C) + (6 * H) + (N) + (O * 4)
y = (C * 3) + (H * 7) + (N) + (O * 2) + (S)

if (n.lower() == "aspartato"):
	print(round(x,2))

else:
	print(round(y,2))
		
