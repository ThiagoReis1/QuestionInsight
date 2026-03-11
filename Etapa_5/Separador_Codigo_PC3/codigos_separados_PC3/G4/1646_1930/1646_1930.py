from numpy import*

v= array(eval(input()))

q=0
t=0

for i in range(size(v)):
	if(v[i]<=50):
		q= q + 1
cont=zeros(q,dtype=int)
for x in range(size(v)):
	if(v[x]<=50):
			cont[t]= x
			t=t+1
				
print(q)
print(cont)
