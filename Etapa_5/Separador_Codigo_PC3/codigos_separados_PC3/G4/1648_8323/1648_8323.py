from numpy import *

freq = array(eval(input()))
rep = 0

for i in range (size(freq)):
	if freq[i] < 70:
		rep += 1

irep = zeros(rep, dtype = int)
j = 0
for i in range (size(freq)):
	if freq[i] < 70:
		irep[j] = i
		j += 1
print(rep)
print(irep)