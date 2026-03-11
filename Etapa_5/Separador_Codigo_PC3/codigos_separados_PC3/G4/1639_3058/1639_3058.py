from numpy import*

v= array(eval(input("Digite a quantidade de alunos matriculados: ")))
soma= 0

for i in range(size(v)):
	if(v[i] % 2 == 0):
		soma= soma + 1
print(soma)

v0= zeros(soma, dtype= int)
j= 0

for i in range(size(v)):
	if(v[i] % 2 == 0):
		v0[j]= v0[j] +  i
		j= j + 1
print(v0)