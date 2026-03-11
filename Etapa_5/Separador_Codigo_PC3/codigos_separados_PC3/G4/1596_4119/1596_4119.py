from numpy import*
v = array(eval(input("notas: ")))
i = 0
s = 0
while (i < size(v)):
	if (v[i] != min(v)):
		s = s + v[i]
	i = i + 1
vt = s/ (size(v) - 1)
print(round(vt,2))
