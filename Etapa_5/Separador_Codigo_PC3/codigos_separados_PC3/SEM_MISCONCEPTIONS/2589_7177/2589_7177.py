from numpy import*
v=array(eval(input("vetor:")))
i=0
count=0
while(i<size(v)-1):
	if(v[i+1]>=v[0]):
		print(i+1)
		count=count+1
	i=i+1
print(count)