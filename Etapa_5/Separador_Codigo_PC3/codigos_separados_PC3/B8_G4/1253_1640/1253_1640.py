from numpy import *

v1 = array(eval(input("Vetor:")))

v2 = zeros(2, dtype = int)
a = min(v1)
b = max(v1)
c = 0.6 * a + 0.4 * b
d = 0.3 * a + 0.7 * b

for j in range(size(v1)):
	if(v1[j] >= a and v1[j] < c):
		v2[0] = v2[0] + 1
	elif(v1[j] >= d and v1[j] < b):
		v2[1] += 1
print(v2)