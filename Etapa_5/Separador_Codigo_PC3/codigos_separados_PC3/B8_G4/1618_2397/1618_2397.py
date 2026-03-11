from numpy import*
v=array(eval(input()))

l=""
i=size(v)-1
j=0
while(j<size(v)-1):
	if(j!=-1) and(j!=(size(v)-2)):
		l=l+ str(v[j]) + "x^" + str(i) +  " + "
	elif(j!=-1) and(j!=(size(v)-1)):
		l=l+ str(v[j]) + "x" + " + "
	i=i-1
	j=j+1
l1=l+ str(v[-1])
print(l1)
	
