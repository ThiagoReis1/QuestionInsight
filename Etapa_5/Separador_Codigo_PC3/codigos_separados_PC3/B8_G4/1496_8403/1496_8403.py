from numpy import *
t = int(input('tempo:'))
x1 = 80
x2 = 90
x3 = 100
x4 = 110

p1 = 3000
p2 = 4000
p3 = 5000
p4 = 6000
if t >= 0 and t <= 100:
	vt = x1 + p1
elif t > 100 and t <= 200:
	vt = t * x2 + p2
elif t > 200 and t <= 300:
	vt = t * x3 + p3
elif t > 300:
	vt = t * x4 + p4
print(round(vt,2))
	
