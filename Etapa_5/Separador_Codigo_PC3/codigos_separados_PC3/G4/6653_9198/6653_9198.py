from numpy import*

v = array(eval(input("Digite: ")))
x = [3,5,1]
r = 0
i = 0
y = 9

while (i < size(v)):
	r += x[i]*v[i]
	i += 1
print(round(r/y, 2))