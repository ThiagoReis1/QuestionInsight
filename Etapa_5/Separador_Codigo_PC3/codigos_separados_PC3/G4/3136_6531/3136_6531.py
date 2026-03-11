from numpy import*
a = array(eval(input()))
m = 0
for i in range(size(a)):
	m = m +(log(a[i] + 1))/(size(a))
print(round(exp(m)-1,2))