var = input()

i = 0
total = 0
d = 0
s = 0
l = 0
while i < len(var):
	if var[i].upper() == "D":
		d += 1
	elif var[i].upper() == "S":
		s += 1
	elif var[i].upper() == "I":
		l += 1
	i += 1

if d > 0:
	total += d * 2.25
if s > 0:
	total += s * 4
if l > 0:
	total += l * 6.90
	
print(round(total, 2), d, s, l)