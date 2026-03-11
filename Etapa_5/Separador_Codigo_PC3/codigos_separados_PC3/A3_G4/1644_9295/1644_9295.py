from numpy import*
v = array(eval(input("")))
ap = 0
rp = 0

for i in range(size(v)):
	if v[i] >= 5.0:
		ap += 1
	else:
		rp += 1
print(rp)
for i in range(size(v)):
	if v[i] < 5.0:
		print(v[i])

