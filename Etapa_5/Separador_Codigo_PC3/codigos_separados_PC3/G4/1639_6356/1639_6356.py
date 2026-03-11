from numpy import *
turm = array(eval(input("Informe quantidade de alunos: ")))
c = 0
j = 0
for i in range(size(turm)):
	if turm[i]%2==0:
		c=c+1
d=zeros(c, dtype=int)
for i in range(size(turm)):
		if turm[i]%2==0:
			d[j]=i
			j=j+1
print(c)
print(d)
			