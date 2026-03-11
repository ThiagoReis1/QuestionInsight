from numpy import*
p = array(input("").upper().split(","))
a = zeros(4, dtype = int)

for v in p:
	if v == "O":
		a[0] += 1
	if v == "D":
		a[1] += 1 
	if v == "N":
		a[2] += 1 
	if v == "C":
		a[3] += 1 
print(a)