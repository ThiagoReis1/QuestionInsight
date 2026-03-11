from numpy import *

d = array(eval(input()))

i = 0
x = 0

while i < len(d):
	if d[i] == 1:
		x += 10
	if d[i] == 2:
		x += 5
	if d[i] == 3:
		x += 10
	if d[i] == 4:
		x += 5
	if d[i] == 5:
		x += 10
	if d[i] == 6:
		x += 5
	i += 1
print(int(x))