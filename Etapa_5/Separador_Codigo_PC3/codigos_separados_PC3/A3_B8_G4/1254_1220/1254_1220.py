from numpy import *
v=array(eval(input("Informe o vetor: ")))
A= min (v)
B= max (v)
C=0.6*A + 0.4*B
D=0.3*A+0.7*B
x=0
cont= zeros(2, dtype(int))
for i in (range(size(v))):
	if(v[i]>=C) and (v[i]<=D):
			 cont[0]=cont[0]+1
	elif (v[i]>=D) and (v[i]<B):
			 cont[1]=cont[1]+1
print(cont)
		