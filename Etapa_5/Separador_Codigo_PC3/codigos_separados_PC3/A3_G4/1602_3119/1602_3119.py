from numpy import*

v = array(eval(input("Tempos de chegada: ")))

i = 0
c = 0

while(i < size(v)):
	if ((v[i]) == max(v)):
		c = v[i]
		print(i)
	i = i + 1
	
	