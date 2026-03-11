from numpy import*
v = array(eval(input("vetor dos corredores: ")))
i = 0
while (i < size(v)):
	if (v[i] == max(v)):
		print(i)
	i += 1