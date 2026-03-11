from numpy import *

p = float(input("qual o valor? "))
x = array(eval(input("qual valor? ")))
y = array(eval(input("qual valor? ")))
t = p/(p-1)
s = 0

for i in range (size(x)):
	s += abs((2*x[i]) - y[i])**t
	d = (s)**(1/t)
	
print(round(d,4))