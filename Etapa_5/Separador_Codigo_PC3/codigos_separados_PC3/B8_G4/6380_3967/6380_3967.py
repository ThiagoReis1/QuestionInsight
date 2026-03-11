from numpy import*
p = input().split(",")

pd = zeros(4, dtype=int)

for i in p:
	if i == "E":
		pd[0] = pd[0] + 1
	elif i == "V":
		pd[1] = pd[1] + 1
	elif i == "A":
		pd[2] = pd[2] + 1
	elif i == "D":
		pd[3] = pd[3] + 1

print(pd)