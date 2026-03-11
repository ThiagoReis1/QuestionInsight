from numpy import *

v = array(eval(input("digite o vetor: ")))
n = size(v)
x = 0
for i in range(n):
	if(v[i] % 10 == 5 and v[i] % 10 == 0):
		x = x + 1
		
y = 0
z = 0

novo[y] = zeros(n, dtype=int)
for i in range(n):
	if(v[i] % 10 == 5 and v[i] % 10 == 0):
		novo[y] = v[i]
		y = y + 1
	
print(x)
print(novo)
		

		
