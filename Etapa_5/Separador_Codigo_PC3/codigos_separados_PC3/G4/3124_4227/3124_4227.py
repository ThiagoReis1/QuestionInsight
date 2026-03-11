from numpy import*
a = array(eval(input("")))
i = 0 
m = 1
while (i<size(a)):
	m = m * a[i]
	i = i + 1
print(round(m**(1/size(a)),2))
