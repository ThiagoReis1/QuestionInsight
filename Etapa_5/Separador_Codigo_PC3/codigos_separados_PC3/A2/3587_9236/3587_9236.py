from numpy import*
v = array(eval(input(" ")))
i = 0
total = 100

while(i <size(v)):
	if (v[i] == 1):
		total = total*5
	elif (v[i] == 2):
		total = total*3
	elif (v[i] == 3):
		total = total
	else:
		total = total/2
	i += 1
print(round(total, 2))