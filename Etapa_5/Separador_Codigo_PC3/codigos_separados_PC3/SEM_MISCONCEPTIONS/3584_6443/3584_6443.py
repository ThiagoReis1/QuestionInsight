from math import *
vet= eval(input())
total = 0
m=0

for i in vet:
	if i < 200:
		total+= 200 - m*(0.15)
		m+= 1
print(round(total,2))
