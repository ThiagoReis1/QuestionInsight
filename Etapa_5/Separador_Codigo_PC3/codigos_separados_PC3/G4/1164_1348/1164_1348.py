n=int(input("digite um numero:"))
a=0
s=1
i=1
c=1
S=0
while(a<n):
	S+=((c**2)/(4+i))*s
	c+=1
	s*=-1
	i+=2
	a+=1
print(round(S,8))
	
