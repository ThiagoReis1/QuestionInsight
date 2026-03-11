from numpy import *
p = array(eval(input(' ')))
i = 0
total = 100
while i < len(p):
	if p[i]==1:
		total = total * 5
	if p[i]==2:
		total = total * 3
	if p[i]==3:
		total = total
	if p[i]==4:
		total = total/2
	i = i + 1
print(round(total, 2))