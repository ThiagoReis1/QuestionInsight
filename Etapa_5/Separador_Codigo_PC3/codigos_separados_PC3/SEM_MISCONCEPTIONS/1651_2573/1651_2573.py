from numpy import *

string = input("Entre com a string: ").split(',')

s = len(string)

cont = zeros(6, dtype=int)

for i in range(s):
	if (string[i] == "MC"):
		cont[0] = cont[0] + 1
	if (string[i] == "C"):
		cont[1] = cont[1] + 1
	if (string[i] == "CM"):
		cont[2] = cont[2] + 1
	if (string[i] == "EM"):
		cont[3] = cont[3] + 1
	if (string[i] == "E"):
		cont[4] = cont[4] + 1
	if (string[i] == "ME"):
		cont[5] = cont[5] + 1
print(max(cont))
print(cont)

