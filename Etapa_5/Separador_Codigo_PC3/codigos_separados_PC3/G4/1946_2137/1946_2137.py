a = input("nome do aminoácido: ").lower()
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

if a == "fenilalanina":
	r = 9*C + 11*H + 2*O + S
	print(round(r,2))
	
if a == "tirosina":
	r = 9*C + 11*H + N + 3*O
	print(round(r,2))
