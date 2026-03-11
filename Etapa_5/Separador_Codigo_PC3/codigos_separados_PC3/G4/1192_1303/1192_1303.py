#Johnathan Dias				#Matricula:21651445
from numpy import*

v=array(eval(input("digite os valores da temperatura:")))

i=0
el=0
while (i<size(v)):
	if (v[i]>=0):
		el=el+1
	i=i+1
v0 = array(zeros(el,dtype=float))
i=0
t=0
while (i<size(v)):
	if (v[i]>=0):
		v0[t]=v[i]
		t= t+1
	i=i+1
print(v0)