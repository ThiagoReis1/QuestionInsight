from numpy import * 

v = array(eval(input("Tempos: ")))

i = 0
c = 0

while (i < size(v)):
	if(v[i] == max(v)):
		n = v[i]
		print(i)
	i = i + 1

	