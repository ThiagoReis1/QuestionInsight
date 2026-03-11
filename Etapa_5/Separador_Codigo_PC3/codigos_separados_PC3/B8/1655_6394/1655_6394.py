from math import *
from numpy import *

states = input("Digite os estados: ").upper().split(',')

cont = zeros(5, dtype=int)

for i in states:
	if(i == "AC"):
		cont[0] += 1
	elif(i == "AM"):
		cont[1] += 1
	elif(i == "PA"):
		cont[2] += 1
	elif(i == "RO"):
		cont[3] += 1
	elif(i == "RR"):
		cont[4] += 1

print(max(cont))
print(cont)