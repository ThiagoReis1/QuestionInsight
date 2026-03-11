#Karoline Oliveira da Costa
#25 de Agosto de 2016
#AV.06 Questão 1
from numpy import*


v=array(eval(input("Vetor: ")))
x=array(zeros(2,dtype=int))
A=min(v)
B=max(v)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
i=0
for i in range(size(v)):
	if(v[i] >= A and v[i] <C):
		x[0]=x[0]+1
		
for i in range(size(v)):
	if(v[i]>= D and v[i]<B):
		x[1]=x[1]+1	
		
		
print(x)