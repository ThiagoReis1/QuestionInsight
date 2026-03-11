from numpy import *
v = eval(input())
i = 0
total = 0
while i < size(v):
	if v[i] == 1:
		total = 10 + total
	if v[i] == 2:
		total = 5 + total
	if v[i] == 3:
		total = 0 + total
	if v[i] == 4:
		total = 5 + total
	if v[i] == 5:
		total = 20 + total
	if v[i] == 6:
		total = 10 + total
	i = i + 1
print(total)