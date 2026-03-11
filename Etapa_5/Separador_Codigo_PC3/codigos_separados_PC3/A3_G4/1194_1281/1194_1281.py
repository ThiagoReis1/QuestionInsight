from numpy import *
v=array(eval(input("temperatura")))
t=size(v)
i=0
j=0
z=array(zeros(t, dtype=float))
while i<t:
	if v[i]>-100:
		j=j+1
	i=i+1	
z=array(zeros(j, dtype=float))
i=0
j=0
while i<t:
	if v[i]>-100:
		z[j]=v[i]
		j=j+1
	i=i+1
print(z)			