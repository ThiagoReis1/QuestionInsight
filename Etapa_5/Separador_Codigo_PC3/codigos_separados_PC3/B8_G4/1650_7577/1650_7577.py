from numpy import*

var = input(": ").split(",")
p = zeros(5, dtype=int)

for x in var:
	if x == "P":
		p[0]=p[0]+1
	elif x == "C":
		p[1]=p[1]+1
	elif x == "R":
		p[2]=p[2]+1
	elif x == "L":
		p[3]=p[3]+1
	elif x == "B":
		p[4]=p[4]+1
		
print(max(p))
print(p)