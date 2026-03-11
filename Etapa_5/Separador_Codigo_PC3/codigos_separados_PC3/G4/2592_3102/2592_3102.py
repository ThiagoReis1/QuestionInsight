from numpy import*
v = array(eval(input("vetor:")))
a = 0

for i in range(1,size(v)):
	if(v[i]>=v[0]):
		a = a+1

for j in range(1,size(v)):
	if(v[j]>=v[0]):
		print(j)

print(a)