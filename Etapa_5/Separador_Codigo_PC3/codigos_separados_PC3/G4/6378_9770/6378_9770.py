from numpy import*
V = array(input("").upper().split(","))
a = zeros(4 , dtype=int)

for v in V:
	if v == "C":
		a[0] += 1
	if v == "D":
		a[1] += 1
	if v == "V":
		a[2] += 1
	if v == "U":
		a[3] += 1
		
print(a)

