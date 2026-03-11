from numpy import*
l=array(eval(input(":")))
a=0
m=sum(l)/size(l)
for i in range(size(l)):
	a=a+(l[i]-m)**2
r=a/(size(l)-1)
x=r**0.5
print(round(x,3))
