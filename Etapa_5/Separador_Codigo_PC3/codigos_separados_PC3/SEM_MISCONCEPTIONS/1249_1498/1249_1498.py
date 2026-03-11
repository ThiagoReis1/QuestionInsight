from numpy import*
v = array(eval(input(""))

a = min(v)
b = max(v)
c = (0.7 * a + 0.3 * b)
d = (0.4 * a + 0.6 * b)

c = 0
c1 = 0
x = 0
for j in range(0, size(v)):
	if(v[j] >= a and v[j] < c ):
		c = c + 1
		x = x + 1
for k in range(0,size(v)):
	if(v[k] >= c and v[k]< d):
		c1 = c1 + 1
x[0]= c
x[1] =c1
print(x)