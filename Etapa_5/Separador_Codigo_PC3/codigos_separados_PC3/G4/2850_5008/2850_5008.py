from numpy import *
v = array(eval(input("v: ")))
s = 0
for i in v:
	s += i
	if s >= 55:
		s = 0
print(s)