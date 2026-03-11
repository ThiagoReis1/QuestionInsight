from numpy import*
v=array(eval(input()))

f=zeros((size(v)),dtype=int)
y=0
for i in range (size(v)):
	f[y]=(v[i])**2
	y+=1
	
print(f)
