from numpy import *

v = array(eval(input()))

i = 0 
j = 1
soma = 0
total = 0
p = 0

while(i < size(v)):
	total = total + v[i]*j
	p = p + j
	soma = p
	t = total / soma
	i = i + 1
	j = j + 1
print(round(t, 2))	