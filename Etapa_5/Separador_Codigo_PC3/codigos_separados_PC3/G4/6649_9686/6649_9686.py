from numpy import*
i= 0
s = 0
v = array([3,2,4,1,3])
a = array(eval(input("")))
while i!= 5:
	b = sum(a[i]*v[i])
	s = s + b
	i = i+1
t = s/13
print(round(t, 2))
	