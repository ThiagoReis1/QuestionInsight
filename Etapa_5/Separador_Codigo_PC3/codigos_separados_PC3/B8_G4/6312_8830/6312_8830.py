from numpy import *
i = 0
B = 3.75
C = 7.9
E = 9.85
Bc = 0
Cc = 0
Ec = 0
Entrada = input("seu vetor: ").upper()
Parada = len(Entrada)

while i < Parada:
	if Entrada[i] == "B":
		#B = B + 3.75
		Bc = Bc + 1
		#i = i + 1
	elif Entrada[i] == "C":
		#C = C + 7.9
		Cc = Cc + 1
	elif Entrada[i] == "E":
		#E = E + 9.85
		Ec = Ec + 1
	i = i + 1
Total = (B*Bc) + (C*Cc) + (E*Ec)

print(round(Total,2), round(Bc,2), round(Cc,2), round(Ec,2))
