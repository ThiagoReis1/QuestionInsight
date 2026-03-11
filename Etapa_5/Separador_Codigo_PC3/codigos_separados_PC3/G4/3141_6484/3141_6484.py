from numpy import*

v = array(eval(input()))
soma = 0 
for i in range(size(v)):
	soma = soma + v[i]**(1/6)
m = (soma/size(v))**6
print(round(m,2))

