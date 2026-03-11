from numpy import*

v = array(eval(input()))
a = 0

for i in range(size(v)):
	if v[i] <= 50:
		a = a + 1
x = zeros(a, dtype = int)
b = 0
for i in range(size(v)):
	if v[i] <= 50:
		x[b] = i
		b = b + 1
print(a)
print(x)