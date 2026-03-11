from numpy import*

p = float(input(" "))
x = array(eval(input(" ")))
y = array(eval(input(" ")))

a = 0
b = 0
c = 0

t = (p)/(p+1)
xy1 = x + y
xy2 = x - y
xy = xy1 - xy2

for i in range(xy):
	a = a + (abs(x[i] + y[i])**t)
	v = **(1/t)
	
print(p,round, 7)
	
	


