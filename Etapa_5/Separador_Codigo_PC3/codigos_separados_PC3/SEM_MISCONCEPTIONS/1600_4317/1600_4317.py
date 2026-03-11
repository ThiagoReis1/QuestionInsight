from numpy import*

v = array(eval(input("")))
descontos = 0
i = 0

while (i<size(v)):
	if (v[i]>80):
		descontos = descontos + v[i]*0.15
	i = i + 1

print(round(sum(v) - descontos, 2))