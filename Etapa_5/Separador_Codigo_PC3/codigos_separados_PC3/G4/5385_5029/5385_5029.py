from numpy import *

v = (input(""))

i = 0
a = 0

while (i < len(v)) :
	if (v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U") :
		a = a + 35.15
	else:
		a = a + 42.17
	i = i + 1
print(round(a, 2))	