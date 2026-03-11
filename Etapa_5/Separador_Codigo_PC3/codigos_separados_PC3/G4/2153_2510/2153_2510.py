from numpy import*
v = array(eval(input("v:")))
z = array(eval(input("z:")))
x = 0

for i in range (size(v)):
	x = x + (v[i]-z[i])**2
y = (x)**(0.5)
print(round(y,4))