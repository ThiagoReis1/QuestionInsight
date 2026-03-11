n = input(":").lower()
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794
if( n == "aspartato"):
	P = (4*C) + (6*H) + N + (4*O)
	print(round(P, 2))
elif( n == "cisteina"):
	r = (3*C) + (7*H) + N + (2*O) + S
	print(round(r, 2))
elif( n == "metionina"):
	s = (5*C) + (11*H) + N + (2*O) + S
	print(round(s, 2))
else:
	print("Entrada: ", n)
	print("Dado Invalido")
