from numpy import*
v= array(eval(input("Digite o vetor: ")))
A=min(v)
B=max(v)
C= ((0.6 * A) + (0.4 * B))
D= ((0.3 * A) + (0.7 * B))
x= array ([0,0])
for i in v:
	if ( i  >= A and i < C):
		x[0]=x[0]+1
	if (i >=D and i<B):
		x[1]=x[1]+1
print(x)		
		 	