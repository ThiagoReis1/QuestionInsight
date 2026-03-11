from numpy import*
v=array(eval(input()))



n=v[0]
p=60
q=0

for i in range(1,size(v)):
	if(v[i]>=n):
		q=q+1
		print(i)
print(q)