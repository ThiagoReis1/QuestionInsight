from numpy import *

etnias = input().split(',')

qtds = array([0, 0, 0, 0, 0])

for et in etnias:
	if et == 'B':
		qtds[0] = qtds[0] + 1
	if et == 'PA':
		qtds[1] = qtds[1] + 1
	if et == 'PR':
		qtds[2] = qtds[2] + 1
	if et == 'A':
		qtds[3] = qtds[3] + 1
	if et == 'I':
		qtds[4] = qtds[4] + 1

print(max(qtds))
print(qtds)