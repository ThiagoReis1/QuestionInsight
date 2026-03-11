from numpy import*
x = array(eval(input("Alunos por turma: ")))
a=0


for i in range (size(x)):
	if (x[i]%2)==1:
		a+=1
print(a)
b=zeros(a, dtype = int)
e = 0
for i in range (size(x)):
	if (x[i]%2)==1:
		b[e]=i
		e+=1
print(b)
