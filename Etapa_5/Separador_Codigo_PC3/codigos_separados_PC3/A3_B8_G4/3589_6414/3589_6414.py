from numpy import*
v = array(eval(input("digite o vetor: ")))
i = 0
x = 0
n = 0
while (i<size(v)):
	if (v[i] == 1):
		n = v[i]
		x = 80
	elif (v[i] == 2):
		x = v[i]
		x = 40
	elif (v[i] == 3):
		x = v[i]
		x = 20
	elif (v[i] == 4):
		x = v[i]
		x = 10
	i = i + 1
print(sum(x))