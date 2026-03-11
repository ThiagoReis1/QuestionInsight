

n=int(input())

i=0
par=0

while(n!=0):
	if(n%2==0):
		par=par+1
		
	i=i+1
	n=int(input())

tot=(par*100)/i
print(i)
print(round(tot,2))