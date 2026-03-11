from numpy import*
t=eval(input())
i=0
c=0
l=0
while i<size(t):
	if t[i]<60 or t[i]>-60:
		c+=1
	i+=1
i=0

t2= zeros(c,dtype=float)
while i<size(t):
	if t[i]<60 and t[i]>-60:
		t2[i]=t[i]
	i+=1
vet2=(zeros(c,dtype=float))
y=0
z=0
while(y<size(t2)):
	if(t2[y]!=0):
		vet2[z]=t2[y]
		z+=1
	y+=1

print(trim_zeros(vet2))
