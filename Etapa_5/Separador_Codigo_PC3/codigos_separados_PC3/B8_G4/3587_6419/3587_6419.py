from numpy import*
x = array(eval(input("aneis: ")))

p = 100
i = 0

while i<size(x):
	if x[i] == 1:
		p = p * 5
	elif x[i] == 2:
		p = p * 3
	elif x[i] == 3:
		p = p + 0
	elif x[i] == 4:
		p = p / 2
	i = i + 1
print(round(p, 2))