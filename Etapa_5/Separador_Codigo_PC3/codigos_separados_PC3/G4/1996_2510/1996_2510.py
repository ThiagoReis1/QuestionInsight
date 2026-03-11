a = input("Nome do aminoácido: ")

O= 15.9994
C= 12.011
N= 14.0067
S= 32.066
H= 1.0079

if (a=="aspartato"):
	x = 4*C + 6*H + N + 4*O
	print(round(x,2))
elif a=="fenilalanina":
	x = 9*C + 11*H + 2*O + S
	print(round(x,2))
elif a=="tirosina":
	x = 9*C + 11*H + N + 3*O
	print(round(x,2))
else:
	x="Dado Invalido"
	print("Entrada:", a)
	print(x)