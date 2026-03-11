from numpy import*
p = array(eval(input()))
q = array(eval(input()))

d = 0
for i in range(size(p)):
	d = d + (p[i] - q[i]) ** 2
D = sqrt(d)

print(round(D, 4))