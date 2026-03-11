from numpy import * 

v = array(eval(input()))

i = 0
s = 0


while (i<size(v)):
	s = s + v[i]
	if s>75:
		s = 75
	i = i + 1
print(s)