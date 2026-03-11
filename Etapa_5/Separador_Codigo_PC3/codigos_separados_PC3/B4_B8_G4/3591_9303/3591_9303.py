from numpy import *
num = eval(input("num: "))

i = 0

for f in num:
	if f == 1:
		i += 10
	elif f == 2:
		i += 5
	elif f == 3:
		i += 10
	elif f == 4:
		i += 5
	elif f == 5:
		i += 10
	elif f == 6:
		i += 5
print(i)
