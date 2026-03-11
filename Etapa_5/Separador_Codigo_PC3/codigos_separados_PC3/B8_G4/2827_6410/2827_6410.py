from numpy import *

n = array(eval(input("valores: ")))
i = 0

while i < size(n):
	if n[i]>4 and n[i]<5:
		n[i] = n[i] - n[i] + 4
	elif n[i]>9 and n[i]<10:
		n[i] = n[i] - n[i] + 10
	i = i + 1
print(n)