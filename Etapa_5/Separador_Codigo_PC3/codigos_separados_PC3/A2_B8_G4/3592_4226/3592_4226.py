from numpy import *
v = array(eval(input(" > ")))
L = len(v)
a = array([0]*L)
for i in range(L):
	a[i] = v[i]
pts = 100
for i in range(L):
	if a[i] == 1:
		pts = pts
	elif a[i] == 2:
		pts = pts*2
	elif a[i] == 3:
		pts = pts/3
	elif a[i] == 4:
		pts = pts*4
	elif a[i] == 5:
		pts = pts/5
	elif a[i] == 6:
		pts = pts*6

pts = round(pts,2)
print(pts)