from numpy import*
x = array(eval(input()))
m = sum(x)/size(x)
a = 0
for i in range(size(x)):
	a = a + (x[i] - m)**2 

a = a/size(x)-1
d = a**0.5
#print(a)
print(round(d,3))
	