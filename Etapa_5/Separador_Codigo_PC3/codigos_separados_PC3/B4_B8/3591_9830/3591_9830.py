from numpy import *

a = array(eval(input(": ")))

i = 0
total = 0

while i < len(a):
	if a[i] == 1:
		total += 10
	elif a[i] == 2:
		total += 5
	elif a[i] == 3:
		total += 10
	elif a[i] == 4:
		total += 5
	elif a[i] == 5:
		total += 10
	elif a[i] == 6:
		total += 5
	i += 1
print(total)

