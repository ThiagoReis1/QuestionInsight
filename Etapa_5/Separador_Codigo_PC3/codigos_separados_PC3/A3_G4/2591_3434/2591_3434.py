from numpy import*
v = array(eval(input("vetor: ")))
i = 1
j = 0
c = 0


while (i < size(v)):
	s = v[0]+v[i]
	print(s)
	if ( s >= -v[0]):
		c = c + 1
	i = i + 1
print(c)