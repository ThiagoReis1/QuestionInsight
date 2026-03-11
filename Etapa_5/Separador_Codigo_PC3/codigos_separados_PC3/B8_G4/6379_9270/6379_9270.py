from numpy import*

c= input("nota: ").split(",")
x= zeros(5, dtype=int)

for i in c:
	if i == "A":
		x[0] += 1
	elif i == "B":
		x[1] += 1
	elif i == "C":
		x[2] += 1
	elif i == "D":
		x[3] += 1
	elif i == "E":
		x[4] += 1
		
print(x)
		