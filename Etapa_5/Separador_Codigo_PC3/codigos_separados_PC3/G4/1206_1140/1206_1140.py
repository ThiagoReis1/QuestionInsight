from numpy import *

v = array(eval(input()))
i = 0 
j = 0
recorde = 8.95
while(i<size(v)):
	if v[i] < recorde :
		j = j + 1 
	i = i + 1 
print(recorde)
print(j)