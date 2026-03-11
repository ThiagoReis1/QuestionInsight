from numpy import*

a = array(eval(input()))
b = ""
c = 0

for i in range(size(a)):
	if(a[i]%2 == 0):
		c = c + 1
		b = b + str(i) + ","
print(c)
print(array(eval(b)))

