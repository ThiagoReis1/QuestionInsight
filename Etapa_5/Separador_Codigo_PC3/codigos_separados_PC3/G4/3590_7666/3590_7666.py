from numpy import*

a = array(eval(input()))
b = array([10,5,0,5,20,10])
c = 0
i = 0

while(i < size(a)):
	c = c + b[a[i] - 1]
	i = i + 1
	
print(c)