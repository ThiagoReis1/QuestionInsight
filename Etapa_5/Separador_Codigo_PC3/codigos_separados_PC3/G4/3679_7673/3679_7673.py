from numpy import * 

n = int(input())

a = ones((n,n), dtype = int)

for i in range(n):
	for j in range(n):
		if(i>j):
			a[i,j]=0
print(a)
	