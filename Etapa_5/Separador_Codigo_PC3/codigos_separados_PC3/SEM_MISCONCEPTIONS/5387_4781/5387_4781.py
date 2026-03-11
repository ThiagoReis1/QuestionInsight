from numpy import *

n = input()

v = ["A","E","I",'O','U']

i = 0
total = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total7 = 0
total8 = 0
total9 = 0

while ( i < size(n)):
	if n[i] == v[0]:
		total = total + 45.12
	else:
		if n[i] == v[1]:
			total = total + 45.12 
	else:
		if n[i] == v[2]:
			total = total + 45.12
	else:
		if n[i] == v[3]:
			total = total + 45.12
	elif n[i] == v[4]:
		total = total + 45.12
	i = i + 1

print(total)
	