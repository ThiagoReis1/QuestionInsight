from numpy import*
x = array(eval(input()))
i = 0
n = 0
y = []
while (size(x)>i):
	if(x[i]>=70):
		n = n + 1
		y.append(i)
	i = i + 1
print(n)
print(array(y))
	