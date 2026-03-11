from numpy import*
v=array(eval(input("vetor de danos:")))
t=size(v)
nk=0
i=0

while(i<t):
	n=nk+1
	dano= v[i]*n
	i=i+1
print(dano)
