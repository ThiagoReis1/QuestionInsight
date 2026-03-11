from numpy import*

j = array(eval(input("")))

i = 0
c = 0

while (i < size(j)):
	if (j[i] == 2 or j[i] == 4 or j[i] == 6):
		c += 600

	elif (j[i] == 1 or j[i] == 5):
		c += 100
	i =+ 1
print(round(c, 2))

