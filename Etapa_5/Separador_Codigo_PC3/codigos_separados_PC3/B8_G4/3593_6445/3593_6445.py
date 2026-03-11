from numpy import *
face = eval(input())
v1 = 200
for x in face:
	if x == 1 or x == 3 or x == 5:
		v1/=2
	elif x == 2 or x == 4 or x == 6:
		v1*=3
print(round(v1,2))
	