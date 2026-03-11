from numpy import*
N = input("Entrada: ").upper()
i=0
contL = 0
contU = 0
contK = 0
contA = 0
while i < len(N):
	if N[i] == "D":
		contL = contL + 2.25
		contU = contU + 1
	elif N[i] == "S":
		contL = contL + 4.00
		contK = contK + 1
	elif N[i] == "I":
		contL = contL + 6.90
		contA = contA + 1
	i = i + 1

contL = (round(contL, 2) )
print(contL, contU, contK, contA)