from numpy import*
a = array(eval(input()))
b = 0
for i in range(size(a)):
	b = b + a[i]
	if(b > 55):
		b = 0
print(b)