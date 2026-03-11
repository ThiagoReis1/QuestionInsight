from numpy import *

n = (eval(input(":")))
i = 0
p = 10000
while i < size(n):
	if n[i] == 1:
		p = p * 2
	elif n[i]== 2:
		p = p + 0
	elif n[i] == 3:
		p = p / 2
	elif n[i] == 4:
		p = p / 4
	i = i + 1
print(round(p,2))