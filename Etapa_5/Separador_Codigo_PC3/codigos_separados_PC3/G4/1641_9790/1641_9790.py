from numpy import * 
t = array(eval(input("alunos por turma: ")))
cont = 0
for i in t:
	if i%3 == 0:
		cont+=1
print(cont)
 
j = 0
v = zeros(cont,dtype=int)
for i in range(size(t)):
	if t[i] % 3 == 0:
		v[j]=i
		j += 1
print(v)

		
		