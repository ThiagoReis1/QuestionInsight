from numpy import *

produto = input("").upper()
i = 0
total = 0
d = 0
s = 0
l = 0

while i < len(produto):
	if produto[i] == "D":
		total = total + 2.25
		d = d + 1
	elif produto[i] == "S":
		total = total + 4.0
		s = s + 1
	elif produto[i] == "I":
		total = total + 6.90
		l = l + 1
	i = i + 1
print(round(total,2),d,s,l)