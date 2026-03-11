from numpy import*
fut = input(":").upper().split(",")
jog = zeros(4, dtype=int)
j = size(fut)

for i in range (j):
	if fut[i] == "A":
		jog[0] += 1
	elif fut[i] == "B":
		jog[1] += 1 
	elif fut[i] == "C":
		jog[2] += 1
	elif fut[i] == "D":
		jog[3] += 1
print(jog)