from numpy import *
x =  array(eval(input("")))
y = [1,2,3,4]

i = 0
t = size(x)-1
v = 100
while i <= t:
	if x[i] == y[0]:
		v = v*5
	elif x[i] == y[1]:
		v = v*3
	elif x[i] == y[2]:
		v = v + 0
	elif x[i] == y[3]:
		v = v/2
	i += 1
print(round(v,2))