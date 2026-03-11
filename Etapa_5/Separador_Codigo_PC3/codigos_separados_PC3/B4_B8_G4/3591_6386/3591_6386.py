from numpy import *
v = array(eval(input("faces: ")))

q = size(v)
p = 0
s = 0

while p <= q - 1:
	if v[p] == 1:
		s = s + 10
	elif v[p] == 2:
		s = s + 5
	elif v[p] == 3:
		s = s + 10
	elif v[p] == 4:
		s = s + 5
	elif v[p] == 5:
		s = s + 10
	elif v[p] == 6:
		s = s + 5
	p = p + 1
print(s)
		