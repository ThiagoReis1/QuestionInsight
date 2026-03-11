from numpy import*
a=input().split(',')
g=len(a)
b=0
c=0
d=0
e=0
f=0
k=0
while(k<g):
	if(a[k]=='AR'):
		b=b+1
	if(a[k]=='BR'):
		c=c+1
	if(a[k]=='CL'):
		d=d+1	
	if(a[k]=='CO'):
		e=e+1
	if(a[k]=='UY'):
		f=f+1		
	k=k+1
nv=array([b,c,d,e,f])	
print(max(nv))
print(nv)

