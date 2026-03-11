from numpy import *

t = input("txt")

i = 0
b = 0

while (i < len(t)):
	
	if(t[i] in "AEIOU"):
		b = b + 35.15
	else:
		b = b + 42.17
	i = i + 1
	
print(round(b, 2))