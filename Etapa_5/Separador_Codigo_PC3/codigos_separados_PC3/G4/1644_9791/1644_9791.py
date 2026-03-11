from numpy import*
t=array(eval(input("qtd de alunos")))
p=0
for i in range(size(t)):
	if t[i]<5:
		p +=1
ind = zeros(p,dtype=int)
print(p)
j=0
for i in range(size(t)):
	if t[i]<5:
		
		ind[j]=i
		j+= 1
print(ind)