na = input("Nome Aminoácido:")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

a = (4 * C + 8 * H + 2 * N + 3 * O)
b = (5 * C + 8 * H + 1 * N + 4 * O)
c = (C * 11 + 11 * H + 2 * N + 2 * O)

if(na.upper() == "ASPARAGINA"):
	print(round(a,2))
elif(na.upper() == "GLUTAMINA"):
	print(round(b,2))
elif(na.upper() == "TRIPTOFANO"):
	print(round(c,2))
else:
	print("Entrada:",na)
	print("Dado Invalido")
	
