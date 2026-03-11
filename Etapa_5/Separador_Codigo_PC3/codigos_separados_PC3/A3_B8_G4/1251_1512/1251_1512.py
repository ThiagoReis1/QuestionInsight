from numpy import*
v = array(eval(input("")))
a = min(v)
b = max(v)
c = (0.7 * a) + (0.3 * b)
d = (0.4 * a) + (0.6 * b)
x = array(zeros(2, dtype = int))
q = 0
p = 0
for i in range(size(v)):
	if (v[i] >= c and v[i] < d):
		q = q + 1
		x[0] = x[0] + 1
	elif(v[i] >= d and v[i] < b):
		x[1] = x[1] + 1
		
print(x)

