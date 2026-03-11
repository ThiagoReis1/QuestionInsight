v0 = int(input(""))
vd = int(input(""))
vf = int(input(""))
va = v0
l = 1000
t = 0

while va > l :
	va = va + vd - vf
	t = t + 1
print(t)