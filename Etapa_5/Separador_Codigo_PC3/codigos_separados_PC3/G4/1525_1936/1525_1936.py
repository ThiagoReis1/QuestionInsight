vi = int(input("volume inicial: "))
vb = int(input("volume bombeado a cadea min: "))
vr = int(input("volume retirado: "))
m = 0
v = vi
while(v>1000):
	v = v + vb - vr
	m = m + 1
print(m)