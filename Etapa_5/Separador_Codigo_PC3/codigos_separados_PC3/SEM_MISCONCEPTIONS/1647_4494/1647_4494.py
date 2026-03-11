from numpy import *

freqs = eval(input())
aprov = 0

for i in range(0, size(freqs)):
	if freqs[i] >= 70:
		aprov += 1
		

indices = zeros(aprov, dtype=int)
j = 0
for i in range(0, size(freqs)):
	if freqs[i] >= 70:
		indices[j] = i
		j+=1
		
print(aprov)
print(indices)