from numpy import*
z = zeros(4,dtype=int)
v = input("").split(",")
for i in v:
	if i == "A":
		z[0] += 1
	elif i == "B":
		z[1] += 1
	elif i == "C":
		z[2] += 1
	elif i == "D":
		z[3] += 1
		
print(z)
