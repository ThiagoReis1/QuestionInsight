from numpy import* 

c= input("").upper()
x = zeros(4,dtype=int)

for i in c: 
	if i == "C":
		x[0] += 1
	elif i == "D":
		x[1] += 1 
	elif i == "V":
		x[2] += 1
	elif i == "U":
		x[3] += 1 

print(x)