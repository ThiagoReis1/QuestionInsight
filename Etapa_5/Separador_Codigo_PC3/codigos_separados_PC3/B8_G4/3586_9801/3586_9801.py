from numpy import *

v = array(eval(input("Vetor? ")))

i = 0
p = 0

while i < size(v):
	if v[i] == 4:
		p = p + 0
	elif v[i] == 3:
		p = p + 20
	elif v[i] == 2:
		p = p + 60
	elif v[i] == 1:
		p = p + 100
	i = i + 1
total = sum(p)
print(round(total, 2))