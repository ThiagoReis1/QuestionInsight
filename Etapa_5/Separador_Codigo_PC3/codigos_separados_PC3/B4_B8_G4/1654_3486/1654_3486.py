from numpy import*
from numpy.linalg import*
n = input('digite uma sigla:')
a = n.split
x = 0
for i in range (a):
	if('AM' == a[i]):
		x = x + 1
		print(x)
	elif('PE' == a[i]):
		x = x + 1
		print(x)
	elif('MG' == a[i]):
		x = x + 1
		print(x)
	elif('SP' == a[i]):
		x = x + 1
		print(x)
	elif('RS' == a[i]):
		x = x + 1
		print(x)
print(max(a))	
print(x)
