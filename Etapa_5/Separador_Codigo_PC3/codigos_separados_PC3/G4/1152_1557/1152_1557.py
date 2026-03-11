nB = int(input("Digite o numero de habitates de Bravos: "))
nP = int(input("Digite o numero de habitantes de Pentos: "))
nPR = int(input("Digite o numero de habitantes de PR: "))
tB = float(input("Digite a taxa de crescimento de Bravos: "))
tP = float(input("Digite a taxa de crescimento de Pentos: "))
tPR = float(input("Digite a taxa de crescimento de PR: "))
x = 1
while (nB + nP < nPR):
	cb = (nB * tB / 100)
	nB = nB + cb 
	cp = (nP * tP /100)
	nP = nP + cp
	cPR = (nPR * tPR / 100)
	nPR = nPR + cPR
	x = x + 1
print(x)
	