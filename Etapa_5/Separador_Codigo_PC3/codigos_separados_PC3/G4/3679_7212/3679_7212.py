from numpy import*

n = int(input())

mt = zeros((n,n),dtype = int)

for i in range(shape(mt)[0]):
	
	for j in range(shape(mt)[1]):
		if(i<=j):
			mt[i,j]=1
print(mt)
		

	
	
	