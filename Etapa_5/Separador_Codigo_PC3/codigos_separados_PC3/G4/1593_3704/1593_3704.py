from numpy import*
n = array(eval(input(': ')))
 
t = 0
x = 0
y = 0

while t < size(n) :
	x = x + (t+1) * n[t]
	y = y + t + 1
	t = t + 1
m = x/y
print(round(m,2))
	