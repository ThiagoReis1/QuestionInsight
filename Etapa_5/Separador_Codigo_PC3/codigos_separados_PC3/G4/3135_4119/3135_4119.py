from numpy import*
v = array(eval(input("vetor: ")))
i = 0
s = 0
while (i < size(v)):
	s = s + ((v[i] ** (1/2)) / size(v))
	i = i + 1
vt = s ** 2
print (round(vt,2))