from numpy import *

N = input("Pacientes: ").split(",")
vcont = array([0, 0, 0, 0])

for e in range(size(N)):
	if N[e] == "O":
		vcont[0] = vcont[0] + 1
	elif N[e] == "D":
		vcont[1] = vcont[1] + 1
	elif N[e] == "N":
		vcont[2] = vcont[2] + 1
	elif N[e] == "C":
		vcont[3] = vcont[3] + 1
print(vcont)