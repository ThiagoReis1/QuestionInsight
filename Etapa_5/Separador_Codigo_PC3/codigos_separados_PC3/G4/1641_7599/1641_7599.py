from numpy import *
al = array(eval(input("alunos:")))
j = 0
for i in range(size(al)):
	if(al[i]%3==0):
		j = j + 1
v0 = zeros(j,dtype=int)
k = 0
for  n in range(size(al)):
	if (al[n]%3==0):
		v0[k] = n
		k = k + 1
print(j)
print(v0)
	
		