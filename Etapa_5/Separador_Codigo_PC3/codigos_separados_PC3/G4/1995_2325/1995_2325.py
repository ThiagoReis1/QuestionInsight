x = input("Aminoacido: ").lower()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if x == "aspartato":
	R = 4*C + 6*H + N + 4*O
	print(round(R,2))
elif x == "cisteina":
	R = 3*C + 7*H + N + 2*O + S
	print(round(R,2))
elif x == "metionina":
	R = 5*C + 11*H + N + 2*O + S
	print(round(R,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")
