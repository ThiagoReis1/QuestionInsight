from numpy import *
v = array(eval(input("Qual o vetor: ")))
c=0
f=0
for i in range(size(v)):
	if(v[i]>=5):
		c=c+1
	f=f+v[i]
print(f)
print(c)