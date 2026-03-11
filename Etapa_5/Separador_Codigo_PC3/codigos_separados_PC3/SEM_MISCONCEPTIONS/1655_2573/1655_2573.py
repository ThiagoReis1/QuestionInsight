from numpy import *

string = input("Entre com a string: ").split(',')

s = len(string)

cont = zeros(5, dtype=int)

for i in range(s):
	if (string[i] == "AC"):
		cont[0] = cont[0] + 1
	if (string[i] == "AM"):
		cont[1] = cont[1] + 1
	if (string[i] == "PA"):
		cont[2] = cont[2] + 1
	if (string[i] == "RO"):
		cont[3] = cont[3] + 1
	if (string[i] == "RR"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
		


