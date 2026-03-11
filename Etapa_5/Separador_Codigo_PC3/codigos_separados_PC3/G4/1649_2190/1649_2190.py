from numpy import*

s = input().split(",")

m = zeros(5, dtype=int)
for i in s:
	if (i == "P"):
		m[0] = m[0] + 1
	if (i == "C"):
		m[1] = m[1] + 1
	if (i == "M"):
		m[2] = m[2] + 1
	if (i == "V"):
		m[3] = m[3] + 1
	if (i == "A"):
		m[4] = m[4] + 1
print(max(m))
print(m)