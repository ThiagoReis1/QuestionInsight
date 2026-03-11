from numpy import*
v = array(eval(input("")))
i = 0
j = 0
while (i < size(v)):
	if (v[i] == 1):
		i = i + 1
		j = j + 10
	elif (v[i] == 2):
		i = i + 1
		j = j + 5
	elif (v[i] == 3):
		i = i + 1
		j = j
	elif (v[i] == 4):
		i = i + 1
		j = j + 5
	elif (v[i] == 5):
		i = i + 1
		j = j + 20
	elif (v[i] == 6):
		i = i + 1
		j = j + 10
print(j)