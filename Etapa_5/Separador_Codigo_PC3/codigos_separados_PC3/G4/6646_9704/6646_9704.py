from numpy import *
x = array(eval(input()))
s = [1,2,3]
i = 0
p = 0
soma = 0
while i < size(x):
	p = p+(x[i]*s[i])
	soma = soma + s[i]
	i += 1
t = p/soma
print(round(t,2))