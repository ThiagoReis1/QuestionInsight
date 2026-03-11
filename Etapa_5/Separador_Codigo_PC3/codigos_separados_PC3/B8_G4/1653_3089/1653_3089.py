from numpy import*
n=input()
v=n.split(',')

a=0
b=0
c=0
d=0
f=0
for i in range(len(v)):
	if(v[i]=="AR"):
		a=a+1
	elif(v[i]=="BR"):
		b=b+1
	elif(v[i]=="CL"):
		c=c+1
	elif(v[i]=="CO"):
		d=d+1
	elif(v[i]=="UY"):
		f=f+1
novo=zeros(5,dtype=int)
for i in range(size(novo)):
	novo[0]=a
	novo[1]=b
	novo[2]=c
	novo[3]=d
	novo[4]=f

print(max(novo))
print(novo)
		