from numpy import*
x = array(eval(input("")))
i = 0
n = 0

for i in range(size(x)):
	if(x[i] >= 5):
		n = n + 1
print(n)
a = 0
v = zeros(n, dtype=int)
for i in range(size(x)):
	if(x[i] >= 5):
		v[a] = i 
		a = a + 1
print(v)