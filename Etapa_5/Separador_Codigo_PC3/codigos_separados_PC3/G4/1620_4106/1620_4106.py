from numpy import *
M=eval(input(""))
p=array(eval(input()))
i=0
t=0
while(i<size(p)):
	t=t+(p[i]*5/100*M[i])
	i=i+1
print(round(t,2))