from numpy import *

v1 = array(eval(input("Quais aneis acertou 7u7?")))
v2 = [1,2,3,4]

i = 0
t = len(v1) - 1
p = 0

while i <= t:
	if v1[i] == 1:
		p += 80
	elif v1[i] == 2:
		p += 40
	elif v1[i] == 3:
		p += 20
	elif v1[i] == 4:
		p += 10
	i += 1
print(p)