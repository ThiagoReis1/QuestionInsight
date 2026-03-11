from numpy import *

v1 = array(eval(input("Tempos de chegada:")))

i = 0 

while (i < size(v1)):
	if (v1[i] == min(v1)):
		i_min = i
	i = i + 1
		
print(i_min)