from numpy import*
senha= array(eval(input(' senha')))
i=0
o=size(senha)
pos=0
while(o>i):
	pos+=1
	i+=1
v=zeros(pos,dtype=int)
i=0
while(o>i):
	x = senha[i]
	v[i] = x*x
	i+=1
print(v)