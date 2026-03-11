from numpy import*

w = array(eval(input()))
p = array([2 , 1 , 5])
f = size(p)
s = 0
i = 0
while i < f:
	m = w[i] * p[i]
	s = s + m
	i = i + 1
print(round(s/sum(p),2))