from numpy import *
v = eval(input("digite o vator: "))
num = []
for x in v:
	if x == 9:
		num.append(0)
	else:
		num.append((x + 1) ** 2)		
print('[' + ' '.join(map(str, num)) + ']')
		