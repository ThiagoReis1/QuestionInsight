from numpy import*

v = array(eval(input()))
a = 0 
i = 0

for i in range(size(v)):
	if(v[i] >= 2000):
		a = a + 1
print(a)

b = 0
x = zeros(a, dtype=int)
for i in range(size(v)):
	if (v[i] >= 2000):
		x[b] = i
		b +=1
print(x)
