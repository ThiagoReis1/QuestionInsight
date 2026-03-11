from numpy import*

n=int(input("n:"))

m=ones((n,n),dtype=int)

#for i in range(vetor):
#print(vetor)
#print(vetor)
for i in range (0,shape(m)[0]):
	for j in range (0,shape(m)[1]):
		if i>j:
			m[i][j]=0
print(m)