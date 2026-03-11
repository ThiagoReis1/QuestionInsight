from numpy import *
v = array(eval(input("digite o vetor: ")))
B = max(v)
A = min(v)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
v2 = array([0,0])
for i in range (size(v)):
	if (v[i] >= A) and (v[i] < C):
		v2[0] = v2[0] + 1
	elif (v[i] <= D) and (v[i] < B):
		v2[1] = v2[0] + 1
print(v2)
		
