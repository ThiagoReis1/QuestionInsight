from numpy import*

w = array(eval(input()))
p = array([1,2,3])
f = size(p)
i = 0
s = 0
while i < f:
	m = w[i] * p[i]
	s = s + m
	i = i + 1
print(round(s/sum(p),2))