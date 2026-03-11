from numpy import*
r = zeros(4, int)
s = input("").upper().split(",")

for x in s:
	if x == "E":
		r[0] = r[0] + 1
	elif x == "V":
		r[1] = r[1] + 1
	elif x == "A":
		r[2] = r[2] + 1
	else:
		r[3] = r[3] + 1
print(r)