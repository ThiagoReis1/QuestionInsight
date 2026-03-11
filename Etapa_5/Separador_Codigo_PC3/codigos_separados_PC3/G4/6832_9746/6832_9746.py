from numpy import *

c = input().upper()

i = 0
x = 0
while i < len(c):
	if c[i] == "H":
		x += 5.4
	if c[i] == "C":
		x += 8.95
	if c[i] == "L":
		x += 4.5
	i += 1
print(round(x, 2))
	