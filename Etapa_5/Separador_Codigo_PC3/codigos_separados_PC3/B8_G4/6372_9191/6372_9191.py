from numpy import*

c=input("digite o item:").split(",")
x=zeros(4,dtype=int)

for i in c:
	if i == "A":
		x[0] += 1
	elif i == "B":
		x[1] += 1
	elif i == "L":
		x[2] += 1
	elif i == "H":
		x[3] += 1
		
print(x)