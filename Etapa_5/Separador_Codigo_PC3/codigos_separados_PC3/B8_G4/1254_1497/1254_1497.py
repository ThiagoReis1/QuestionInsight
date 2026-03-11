from numpy import*
v = array(eval(input("")))
a = min(v)
b = max(v)
c = 0.6 * a + 0.4 * b
d = 0.3 * a + 0.7 * b

z = array(zeros (2, dtype = int))
for x in range(size(v)):
	if(v[x] >= c and v[x] < d):
		z[0] = z[0] + 1
	elif(v[x] >= d and v[x] < b):
		z[1] = z[1] + 1
print(z)

for i in range(size(x)):
	b = (abs(x[i]) ** t) + b
for i in range(size(y)):
	b2 = (abs(y[i]) ** t) + b2
b = b ** t
b2 = b2 ** t
norma = 7 * (b - b2)
print(norma)
