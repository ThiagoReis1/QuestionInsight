from numpy import*

x = array(eval(input("X: ")))
i = 0

while i < size(x):
	if x [i] > 50:
		x [i] = x[i] - (x[i]*0.08)	
	if x [i] < 50:
		x [i] = x[i]
	i = i + 1

p = sum(x)

print(round(p,2))
		

