v = float(input())
vb = float(input())
vr = float(input())

t = 0

while v > 1000:
	v = v + vb - vr
	t = t + 1
print(t)