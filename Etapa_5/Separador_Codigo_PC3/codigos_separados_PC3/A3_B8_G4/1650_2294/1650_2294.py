from numpy import *
c = input("").split(',')
t = 0
P = 0
C = 0
R = 0
L = 0
B = 0
for i in c:
	if i == "P":
		P = P+ 1
	elif i == "C":
		C = C+ 1
	elif i == "R":
		R = R+ 1
	elif i == "L":
		L = L+ 1
	elif i == "B":
		B = B+ 1
	t = L
print(t)
z = array([P,C,R,L,B])
print(z)
	