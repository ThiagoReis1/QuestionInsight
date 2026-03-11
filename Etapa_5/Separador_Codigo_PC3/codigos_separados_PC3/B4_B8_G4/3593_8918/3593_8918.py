from numpy import*
v = array(eval(input("Digite a face: ")))
i = 0
c = 200

while (i < size(v)):
	if v[i] == 1:
		c = c / 2
	elif v[i] == 2:
		c = c * 3
	elif v[i] == 3:
		c = c / 2
	elif v[i] == 4:
		c = c * 3
	elif v[i] == 5:
		c = c / 2
	elif v[i] == 6:
		c = c * 3
	i = i + 1
print(round(c, 2))
	