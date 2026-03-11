from numpy import *

v = array(eval(input("digite:")))
v1 = [1,3,2,5]
soma = 11
i = 0

while i < size(v):
	nota = v[0]*v1[0] + v[1]*v1[1] + v[2]*v1[2] + v[3]*v1[3]
	nota = nota/soma
	i += 1
print(round(nota,2))
