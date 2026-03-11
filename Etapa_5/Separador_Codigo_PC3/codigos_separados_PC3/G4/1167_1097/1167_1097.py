N=int(input())
s=0
i=1
while(i<=N):
	s=s+((-1)**(i)*(i)**2/(7+(2*i-1)))
	i=i+1
print(round(s, 11))