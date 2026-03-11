from numpy import*
v = array(eval(input("Din:")))

a = 0
for i in v:
	if(i>=2000):
		a = a + 1
print(a)

h = zeros(a, dtype= int)
b = 0
c = 0
for j in v:
	if(j>=2000):
		h[c]= h[c]+ b
		b = b + 1
		c = c+1
	else:
		b = b +1
print(h)