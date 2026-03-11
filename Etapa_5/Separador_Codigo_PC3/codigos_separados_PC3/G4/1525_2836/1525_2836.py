v0 = int(input())
vB = int(input())
vT = int(input())
t = 0
vM = v0
while (vM > 1000):
	vM = vM + vB - vT
	t = t + 1
print(t)