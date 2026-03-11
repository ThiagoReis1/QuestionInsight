from numpy import*
a= array(eval(input()))
m=0
for i in range(size(a)):
	m=m+(exp(a[i]))/exp(size(a))
print(round(log(m),2))