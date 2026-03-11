from numpy import*

x = array(eval(input("Digite: ")))
i = 0
c = 0

while (i < size(x)):
	if (x[i] == 1):
		c += 80
	elif (x[i] == 2):
		c += 40
	elif (x[i] == 3):
		c += 20
	elif (x[i] == 4):
		c += 10
	i += 1
print(c)