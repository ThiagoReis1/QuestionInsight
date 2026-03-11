from numpy import*

v = array(eval(input("digite o vetor:")))
i = 0
c = 0

while (i < size(v)):
	if (v[i] == 1):
		c = c + 10
	elif (v[i] == 2):
		c = c + 5
	elif (v[i] == 3):
		c = c + 10
	elif (v[i] == 4):
		c = c + 5
	elif (v[i] == 5):
		c = c + 10
	elif (v[i] == 6):
		c = c + 5
	i += 1
print(c)
		