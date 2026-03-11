
X = input("Tipo:")
X2 = int(input("QTDE:"))
X3 = int(input("QTDE:"))

P1 = X2 * 13.50
P2 = X3 * 3.00
PF = P2 + P1

# N
L1 = X2 * 6.00
LF = L1 + P2

if X == 'L':
	print(round(LF,2))
else:
	print(round(PF,2))


