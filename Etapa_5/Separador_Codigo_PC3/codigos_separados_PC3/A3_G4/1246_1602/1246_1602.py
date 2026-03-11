from numpy import*
v=array(eval(input("vetor:")))
a=min(v)
b=max(v)
c=(((a*0,75))+(b*0,25))
d=(((a*0,25))+(b*0,75))
i=0
j=0
k=0
for i in range (size(v)):
	if( ( a >=v[i] ) and  ( c <= v[i]) ):
		j=j+1
	if( ( c >= v[i] ) and ( b <= v[i] ) ):
		k=k+1
vet=array[j,k]
print(vet)
	
		

	

		
		