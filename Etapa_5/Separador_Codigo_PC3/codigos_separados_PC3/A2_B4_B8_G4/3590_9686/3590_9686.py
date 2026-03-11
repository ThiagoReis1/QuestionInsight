from numpy import *
a = array(eval(input("")))
i = 0
s = 0
while i < len(a):
	if a[i] == 1:
		s = s + 10
	elif a[i] == 2:
		s = s + 5
	elif a[i] == 3:
		s = s
	elif a[i] == 4:
		s = s + 5
	elif a[i] == 5:
		s = s + 20
	elif a[i] == 6:
		s = s + 10
	i = i + 1
print(s)