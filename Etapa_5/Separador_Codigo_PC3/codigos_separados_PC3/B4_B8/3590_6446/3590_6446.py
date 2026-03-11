from numpy import *
face = array(eval(input()))
total = 0
for i in face:
	if i == 1:
		total += 10
	elif i == 2:
		total += 5 
	elif i == 3:
		total += 0
	elif i == 4:
		total += 5
	elif i == 5:
		total += 20
	elif i == 6:
		total += 10
print(total)