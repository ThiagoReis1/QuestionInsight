from numpy import *
p = array(eval(input("vetor p: ")))
q = array(eval(input("vetor q: ")))
i = 0
k = 0
j = 0
x = 0
while(i != size(p)):
	x += ((p[k] - q[k])**2)
	k = k + 1
	i = i + 1
j = x**0.5
print(round(j,4))

	