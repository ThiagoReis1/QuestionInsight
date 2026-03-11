from numpy import*
a=array(eval(input()))
for i in range(size(a)):
	if a[i]==0:
		for j in range(i):
			a[j]=0
print((sum(a)))