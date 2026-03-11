from numpy import*
x = array(eval(input("item: ")))
i = 0
n = 0
y = 0
z = 80.0
while (i < size(x)):
	if(x[i] > z):
		y = x[i]
		n = n + (y - 0.15)*y
	else:
		n = n 
	i = i + 1
print(sum(n))