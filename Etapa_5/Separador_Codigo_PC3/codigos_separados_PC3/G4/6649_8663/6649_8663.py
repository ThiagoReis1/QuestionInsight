from numpy import*
n = array(eval(input()))
p = [3, 2, 4, 1, 3]
i = 0
num = 0
den = 0
while i < size(p):
	num =num + n[i]*p[i]
	den = den + p[i]
	i += 1
print(round((num/den), 2))