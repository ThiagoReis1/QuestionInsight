from numpy import*

v = array(eval(input("v: ")))
v1 = array(zeros(2, dtype = int))

a = min(v)
b = max(v)
c = 0.75 * a + 0.25 * b
d = 0.25 * a + 0.75 * b

x1 = 0
x2 = 0
			
for i in range(size(v)):
	if(v[i] >= a and v[i] < c):
		x1 = x1 + 1
	elif(v[i] >= c and v[i] < d):
		x2 = x2 + 1
	v1[0] = x1
	v1[1] = x2
print(v1)

