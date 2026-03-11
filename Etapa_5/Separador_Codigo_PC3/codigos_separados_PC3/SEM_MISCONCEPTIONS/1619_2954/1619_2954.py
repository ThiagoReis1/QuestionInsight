from numpy import*

t=array(eval(input()))
b=array(input())
Q=90
M=45
F=0
s=size(t)
i=0
p=0.005
q=0
m=0
f=0

while(i<s):
	if(b[i]=="QUENTE"):
	q=t*Q*p
	if(b[i]=="MORNO"):
	m=t*M*p	
	if(b[i]=="FRIO"):
	f=t*F*p	
	
