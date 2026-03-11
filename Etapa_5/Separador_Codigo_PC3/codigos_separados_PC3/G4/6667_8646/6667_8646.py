from numpy import *

sec = zeros(10, dtype=float)
cont = 0

for i in range(size(sec)):
	a = float(input())
	sec[i] += a
	
M_Not = float(input())

for i in range(size(sec)):
	if sec[i] >= M_Not:
		cont += 1
		
secc = zeros(cont, dtype=float)
cc = 0

for i in rande(size(sec)):
	if sec[i] >= M_Not:
		secc[cc] = sec[i]
		cc += 1

print(cont)
print(secc)