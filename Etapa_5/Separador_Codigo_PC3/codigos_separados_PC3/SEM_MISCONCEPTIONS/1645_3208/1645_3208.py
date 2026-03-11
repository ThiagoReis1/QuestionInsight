from numpy import*
v=array(eval(input()))
d=0
for i in range(size(v)):
	if(v[i]>=2000):
		d+=1
print(d)

x=zeros(3,dtype=int)
for i in range(size(v)):#
	if(v[i]<2000):
		x[0]+=0
	elif(v[i]>=2000):
		x[1]+=1
   elif v[i] > 2000 :
		x[2]+=1
	
print(x)

	
		