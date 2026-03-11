a = "Aspartato"
c = "Cisteina"

n = input()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if (n == a.lower()):
	p = 4 * C + 6 * H + N + 4 * O
	print(round(p,2))
else:
	p2 = 3 * C + 7 * H + N + 2 * O + S
	print(round(p2,2))
	