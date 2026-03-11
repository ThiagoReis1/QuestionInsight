from numpy import*
vt = array(eval(input()))
ps = array([1,2,3])
tam = size(vt)

i = 0
soma = 0
while i < tam:
	m = vt[i] * ps[i]
	soma = soma + m
	i += 1
print(round(soma/sum(ps),2))