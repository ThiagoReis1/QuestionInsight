n=int(input(""))
i=0
j=0
while(n!=0 and n>0):
	j=j+1
	if(n%2==0):
		i=i+1
		
	n=int(input(""))
	
print(j)
print(round((100/j)*i,2))