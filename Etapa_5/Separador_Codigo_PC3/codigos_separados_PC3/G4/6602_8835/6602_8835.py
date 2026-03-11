# faça seu código aqui!
n = int(input(""))
C = 0
P = 0
L = 0
cont = 0
while cont != n:
	cont += 1
	pr = input("").upper()
	if pr == "C":
		C += 1
	if pr == "P":
		P += 1
	if pr == "L":
		L += 1
print("L=", L)
print("C=", C)
print("P=", P)