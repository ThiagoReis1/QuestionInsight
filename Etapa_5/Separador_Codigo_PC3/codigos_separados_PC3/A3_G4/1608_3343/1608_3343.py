from numpy import*

v = array(eval(input("vetor numero de pessoas que entram e saem:")))
l = 75
i = 0
total = 0

while(i < size(v)):
	total = total + v[i]
	
	i = i + 1
print(total)