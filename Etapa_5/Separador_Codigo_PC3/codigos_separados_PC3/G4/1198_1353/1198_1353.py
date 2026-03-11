from numpy import*

a=eval(input())
x=0
cont=0
vec=zeros(size(a),dtype=float)
while(x<size(a)):
	if(a[x]>10):
		vec[x]=a[x]
		cont=cont+1
	x=x+1
vec2=(zeros(cont,dtype=float))
y=0
z=0
while(y<size(vec)):
	if(vec[y]>0):
		vec2[z]=vec[y]
		z=z+1
	y=y+1
print(vec2)
		