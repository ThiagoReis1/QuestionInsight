from numpy import *
v=array(eval(input("insira v: ")))
i=0
j=0
while i<size(v):
	if not (v[i]<-60 or v[i]>60):
		j=j+1
	i=i+1
z=array(zeros(j,dtype=float))
i=0
j=0
while i<size(v):
	if not (v[i]<-60 or v[i]>60):
		z[j]=v[i]
		j=j+1
	i=i+1
print(z)