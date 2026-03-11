from numpy import*
v = array(eval(input("vetor:")))
x = array(zeros(2, dtype = int))
a = min(v)
b = max(v)
c = 0.6*a + 0.4*b
d = 0.3*a + 0.7*b
for r in range(size(v)):
	if v[r] >= a and v[r] < c:
		x[0] = x[0] + 1
	elif v[r] >= c and v[r] < d:
		x[1] = x[1] + 1

print(x)