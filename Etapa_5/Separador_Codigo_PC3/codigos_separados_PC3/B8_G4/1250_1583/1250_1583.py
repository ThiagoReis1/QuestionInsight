from numpy import *
v = array(eval(input("Digite o vetor: ")))
A = min(v)
B = max(v)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
m = 0
n = 0
for i in v:
	if((i >= A) and (i < C)):
		m = m + 1
	elif((i > D) and (i < B)):
		n = n + 1
	k = array([m,n])
print(k)