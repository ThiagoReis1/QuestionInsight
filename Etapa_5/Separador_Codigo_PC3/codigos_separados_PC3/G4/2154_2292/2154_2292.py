from numpy import*
v = array(eval(input()))
v1 = array(eval(input()))
b = 0
for i in range(size(v)):
	b = b + (v1[i] - v[i]) ** 2
b = 1/(1 + sqrt(b))
print(round(b, 4))
