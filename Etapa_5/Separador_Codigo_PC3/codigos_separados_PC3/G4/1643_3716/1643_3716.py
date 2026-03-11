from numpy import*

v= array(eval(input()))
a=0
for i in range (size(v)):
	if v[i]>=5:
		a+=1
		
f=zeros(a,dtype=int)
y=0
for i in range (size(v)):
	if v[i]>=5:
		f[y]=i
		y+=1

print(a)
print(f)
