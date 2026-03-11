from numpy import *

x = array(eval(input("Digite: ")))

a = zeros(size(x), dtype=int)
b = 0
c = 0

for i in range(size(x)):
	if x[i] < 5:
		b += 1
v = zeros(b, dtype=int)
c = 0
print(b)
for i in range(size(x)):
	if x[i] < 5:
		v[c] = i
		c += 1
print(v)

