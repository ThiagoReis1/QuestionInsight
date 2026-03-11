from numpy import*
v=array(eval(input("")))
i=0
j=0
temp=-100
while(i<size(v)):
	if(v[i]<temp):
		j=j+1
	i=i+1
v2=array(zeros(, dtype=float))
i=0
t=0
while(i<size(v)):
	if(v[i]<temp):
		v2[t]=v[i]
		t=t+1
	i=i+1
print(v)