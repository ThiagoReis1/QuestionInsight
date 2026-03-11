from numpy import*
v=eval(input())
n=int(input())
i=0
q=0
while i<size(v):
	if v[i]==n:
		print(i)
	if v[i]>n:
		q+=1
	i+=1
print(q)