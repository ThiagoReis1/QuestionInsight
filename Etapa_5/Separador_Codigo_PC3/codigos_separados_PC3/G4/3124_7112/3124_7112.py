from numpy import*

a = array(eval(input()))

b = 1


for i in range(size(a)):
	b = a[i] * b

	
m = b**(1/size(a))
print(round(m,2))


	
