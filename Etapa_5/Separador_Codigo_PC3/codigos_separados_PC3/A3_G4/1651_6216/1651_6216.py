from numpy import *
string = input("Tom de pele: ").split(",")

MC = 0
C = 0
CM = 0
EM = 0
E = 0
ME = 0

x = zeros(6, dtype=int)
for i in range(size(string)):
	if string[i] == "MC":
		x[0] +=1
	if string[i] == "C":
		x[1] +=1
	if string[i] == "CM":
		x[2] +=1
	if string [i] == "EM":
		x[3] += 1
	if string [i] == "E":
		x[4] += 1
	if string [i] == "ME":
		x[5] += 1

print(max(x))		
print(x)

	

