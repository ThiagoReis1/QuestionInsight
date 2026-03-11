v0 = int(input("volume inicial: "))
vb = int(input("bombeado para dentro: "))
vr = int(input("elfa tirou: "))

t = 1
v0 = 5000

while(v0 >= 1000):
	v0 = v0 + vb / t
	t = t + 1

print(t)