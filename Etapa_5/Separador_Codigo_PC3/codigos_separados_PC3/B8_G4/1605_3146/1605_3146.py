from numpy import*
m=array(eval(input( )))

i=200
acum=0

while i<size(m):
	if m[i]==1:
		m[i]= i*4
	elif m[i]==2:
		m[i]= i*2
	elif m[i]==3:
		m[i]=i
	elif m[i]==4:
		m[i]= i/2
	acum=acum+m[i]
	i=i*1
	
print(round(sum(m),2))