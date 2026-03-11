Z = int(input())
H = int(input())
X = int(input())
Y = int(input())

popZ = Z
popH = H
d = 0
while(popH != 0 or popZ != 0):
	popH = popH - popZ * X
	popZ = popZ - popH * Y
	d = d + 1
	
print(d)
