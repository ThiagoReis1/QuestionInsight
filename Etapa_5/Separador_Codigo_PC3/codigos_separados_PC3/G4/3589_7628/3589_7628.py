from numpy import*
a=array(eval(input()))

i=0
v=zeros(size(a))
while i<size(a):
	if a[i]==1:
		v[i]=80
	if a[i]==2:
		v[i]=40
	if a[i]==3:
		v[i]=20
	if a[i]==4:
		v[i]=10
	i=i+1
	b=sum(v)
	b=int(b)
print(b)