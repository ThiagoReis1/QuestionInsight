from numpy import*
v=array(eval(input( )))

i=0
acum=0

while i<size(v):
	if v[i]==1:
		v[i]=80
	elif v[i]==2:
		v[i]=40
	elif v[i]==3:
		v[i]=20
	elif v[i]>=4:
		v[i]=0
	acum=acum+v[i]
	i=i+1
	
print(sum(v))

		