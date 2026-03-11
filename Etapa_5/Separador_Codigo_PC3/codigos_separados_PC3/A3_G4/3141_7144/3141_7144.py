from numpy import*

v = array(eval(input()))
soma = 0
p = 0

for i in range(size(v)):
	soma = soma + v[i]**(1/6)
	p = (soma/size(v))**6
print(round(p, 2))
