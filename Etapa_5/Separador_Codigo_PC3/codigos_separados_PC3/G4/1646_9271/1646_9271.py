from numpy import *

d = array(eval(input("Digite os valores dos depositos: ")))
s = 0

for i in range(size(d)):
	if d[i] <= 50.0:
		s = s + 1
print(s)

c = zeros(s, dtype=int)
j = 0

for i in range(size(d)):
	if d[i] <= 50.0: 
		c[j] = i
		j = j + 1
print(c)