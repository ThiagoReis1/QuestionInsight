from numpy import*		
v=array(eval(input("Saques:")))
t=size(v)
cont=0
for i in range(t):
	if(v[i]>=2000):
		cont=cont+1
c=arange(cont)
j=0
for i in range(t):
	if(v[i]>=2000):			
			c[j]=i
			j=j+1

print(cont)
print(c)
	