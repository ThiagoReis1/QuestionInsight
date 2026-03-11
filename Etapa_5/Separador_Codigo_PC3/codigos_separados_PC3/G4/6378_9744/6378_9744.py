from numpy import*
v = input().upper().split(",")
z = zeros(4, dtype=int)
for i in v:
	if i == "C":
		z[0]+=1 
	if i == "D":
		z[1]+=1
	if i == "V":
		z[2]+=1
	if i == "U":
		z[3]+= 1
print(z)