from math import*
b = eval(input(": "))
n = float(input(": "))
t = 0
a = 0
s = +1
while(t<n):
	a = a+ s*(b*(2*t))/factorial(2*t)
	t = t+1
	s = -s
x= cos(a)
print(x)
	