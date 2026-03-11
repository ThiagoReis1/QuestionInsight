from numpy import*
x= array(eval(input()))
m= sum(x)/size(x)

for i in range(size(x)):
	d= ((x[i]-m)**2)/x[-1]-1
	d= sum(d)
	print(round(d,3))
	