from numpy import *

m = array(eval(input("calcular media: ")))
p = array([5,4,3,2])

i = 0
soma = 0

while i < size(m):
	soma = soma + (m[i] * p[i])
	i = i + 1
print(round(soma/sum(m), 2))