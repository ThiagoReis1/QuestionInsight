from numpy import*

a = array(eval(input("quantidade de alunos matriculados: ")))

par = 0
for i in range(size(a)):
	if(a[i]%2==0):
		par = par + 1 
print(par)



v = zeros(par,dtype=int)
j = 0
i = 0
for j in range(size(a)):
	if(a[j]%2==0):
		v[i]= j
		i = i+1
print(v)