from numpy import *
r = array(eval(input("R: ")), dtype=int)
c = 0
t = 10000
while c < len(r):
	if r[c] == 1:
		t = t*2
	elif r[c] == 2:
		t = t
	elif r[c] == 3:
		t = t/2
	elif r[c] == 4:
		t = t/4
	c += 1

print(round(t,2))