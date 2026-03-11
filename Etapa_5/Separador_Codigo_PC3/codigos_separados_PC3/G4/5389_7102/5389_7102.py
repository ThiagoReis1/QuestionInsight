from numpy import *

v = input().upper()
i = 0
s = 0

for i in range(0, len(v)):
	if v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U":
		s = 3.15 + s
	else:
		s = 4.17 + s
print(round(s,2))