from numpy import *

v = array(eval(input("vetor:")))
c = array([2,2,6,1])

i = 0 
soma = 0 

while i < size(v):
	s = v[i]*c[i]
	soma = soma + s
	i+=1
print(round(soma/sum(c),2))