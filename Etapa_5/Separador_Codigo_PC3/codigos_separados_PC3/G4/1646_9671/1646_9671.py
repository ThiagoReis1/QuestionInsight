from numpy import *

saque = array(eval(input("insira o valor do saque: ")))

c = 0

for i in range(size(saque)):
	if saque[i] <= 50:
		c = c + 1

v = zeros(c, dtype=int)
x = 0

for i in range(size(saque)):
	if saque[i] <= 50:
		v[x] = i
		x = x + 1
		
print(c)
print(v)