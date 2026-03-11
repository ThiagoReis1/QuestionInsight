from numpy import*
v=array(eval(input("")))
m=0
p=0
p1=0
d=0
m=sum(v)/size(v)
for i in range(size(v)):
	p=p+((v[i]-m)**2)
	
d=(p/(size(v)-1))**0.5
print (round(d,3))	