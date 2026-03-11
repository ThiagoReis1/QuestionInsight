from numpy import*

v = array(eval(input("saques:")))
a = 0
for i in range(size(v)):
	if(v[i] >= 2000):
		a = a + 1
print(a)
j = 0
b = zeros(a, dtype=int)
for i in range(size(v)):
	if(v[i] >= 2000):
		b[j] = i
		j = j + 1
print(b)