from numpy import *

x = array(eval(input("Andares:")))

a = 1;
t = 1;
m = 0;

while t<size(x):
	m = m + abs(x[t] - x[t-1])*3
	t = t+1
print(m)