from numpy import*

v = array(eval(input()))

m = 0
for i in range(size(v)):
	m = m + (log(v[i]+1))/(size(v))
print(round(exp(m)-1, 2))