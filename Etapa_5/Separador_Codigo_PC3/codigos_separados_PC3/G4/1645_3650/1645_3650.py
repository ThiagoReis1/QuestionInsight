from numpy import*
saque= array(eval(input('valor do saque')))
i=0
o=size(saque)
g=0
while(i<o):
	if(saque[i]>=2000):
		g=g+1
	i=i+1
i=0
v=zeros(g,dtype=int)
z=0
while(i<o):
	if(saque[i]>=2000):
		v[z]=i
		z=z+1
	i=i+1
print(g)
print(v)
	

	