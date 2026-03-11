from numpy import *

v = array(eval(input("digite as notas: ")))

r = 0
b = 0

for i in range(size(v)):
	if(v[i] < 70):
		r = r + 1
		
n = zeros(r, dtype=int)		
for i in range(size(v)):
	if(v[i] < 70):
		n[b] = i
		b = b + 1
print(r)
print(n)
		