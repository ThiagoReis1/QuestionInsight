n=int(input("Digite um numero: "))
a=0
s=0
i=3
b=1
sinal=-1	
c=sqrt(b)
while(a<n):
	s=s+((c*sinal)/(6+i))
	i=i+2
	c=b+1 
	a=a+1
print(round(s,8))