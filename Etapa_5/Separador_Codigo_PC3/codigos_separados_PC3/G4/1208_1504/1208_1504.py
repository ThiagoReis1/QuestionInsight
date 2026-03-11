from numpy import *

v = array(eval(input("digita os saltos:")))
k = 0
i = 0
recorde = 98.48
while( i <= (size(v)-1)):
	if (v[i] <= recorde):
		k = k + 1 
	i = i + 1	
recorde = 98.48
print(recorde)
print(k)