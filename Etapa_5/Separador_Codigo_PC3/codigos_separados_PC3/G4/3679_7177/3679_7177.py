from numpy import*
x=array(eval(input("x:")))
v=zeros((x,x),dtype=int)
for i in range(x):
	for j in range(x):
		if(i<j or i==j):
			v[i,j]=1
		else:
			v[i,j]=0
print(v)
