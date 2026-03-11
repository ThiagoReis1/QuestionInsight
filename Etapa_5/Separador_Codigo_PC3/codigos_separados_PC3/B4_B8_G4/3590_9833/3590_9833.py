from numpy import *
	
a = array(eval(input()))
i = 0
so = 0
while i < size(a):
	if a[i] == 1:
		so = so + 10
	elif a[i] == 2:
		so = so + 5
	elif a[i] == 3:
		so = so + 0
	elif a[i] == 4:
		so = so + 5
	elif a[i] == 5:
		so = so + 20
	elif a[i] == 6:
		so = so + 10
	i = i + 1
print(round(so,2))