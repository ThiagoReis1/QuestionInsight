from numpy import *
v = array(eval(input("")))
A = min(v)
B = max(v)
C = (0.65 * A) + (0.35 * B)
D = (0.45 * A) + (0.55 * B)
x = array(zeros(2, dtype = int))
q = 0
p = 0
for i in range(size(v)):
	if ((v[i] >= A) and (v[i] < C)):
		q = q + 1
		x[0] = q
	elif ((v[i] >= C) and (v[i] < D)):
		p = p + 1
x[1] = p
print(x)