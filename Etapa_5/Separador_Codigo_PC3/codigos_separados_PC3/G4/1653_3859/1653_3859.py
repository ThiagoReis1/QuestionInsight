#Evento Sul-Americano

from numpy import *

nac = (input("Nacionalidade: ")).upper().split(',')
print(nac)
n = zeros(5, dtype=int)
for i in range(size(nac)):
	if nac[i] == "AR":
		n[0] = n[0] + 1
	elif nac[i] == "BR":
		n[1] = n[1] + 1
	elif nac[i] == "CL":
		n[2] = n[2] +1
	elif nac[i] == "CO":
		n[3] = n[3] +1
	else:
		n[4] =n[4]+1
print(n)