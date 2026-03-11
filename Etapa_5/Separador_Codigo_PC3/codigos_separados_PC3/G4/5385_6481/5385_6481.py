from numpy import *

string = input().upper()

i = 0
v = 0
c = 0

while (i < len(string)):
	if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
		c = c + 35.15
	else:
		v = v + 42.17
	i = i + 1
		
cont = c + v
print(round(cont, 2))
 
