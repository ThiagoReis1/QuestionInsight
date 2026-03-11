from numpy import*
a  = array(eval(input()))
b = []
c = 0
for i in range (size(a)):
	if a[i] >= 5:
		b.append(i)	
		c= c + 1
print(c)
print(array(b))
