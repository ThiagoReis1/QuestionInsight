from numpy import*

c = input("nota:").split(",")
x= zeros(4,dtype=int)


for i in c:
	if i == "C":
		x[0] += 1
	if i == "D":
		x[1] += 1
	if i == "V":
		x[2] += 1
	if i == "U":
		x[3] += 1
		
print(x)