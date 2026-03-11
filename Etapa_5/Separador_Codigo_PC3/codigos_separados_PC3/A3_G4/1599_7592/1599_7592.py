from numpy import*

v1 = array(eval(input()))


if(v1.any() > 80):
	a= v1.any() * (15/100)
	
else:
	a= v1
	
b=sum(v1)
print(b)
	