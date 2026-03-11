from numpy import *
s = input().split(',')

contc = 0
contj = 0
contk = 0
contm = 0
contt = 0

for i in s:
	if i == 'CHN':
		contc = contc + 1
	elif i == 'JPN':
		contj = contj + 1
	elif i == 'KOR':
		contk = contk + 1
	elif i == 'MGL':
		contm = contm + 1
	else:
		contt = contt + 1
a = array([contc , contj , contk, contm, contt])
print(max(a))
print(a)

