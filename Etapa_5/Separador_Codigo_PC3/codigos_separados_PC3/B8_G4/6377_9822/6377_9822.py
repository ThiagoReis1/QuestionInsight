from numpy import*

gol = input().upper().split(",")
jog = zeros(4, dtype=int)

for i in gol:
	if i == "A":
		jog[0] += 1
	elif i == "B":
		jog[1] += 1
	elif i == "C":
		jog[2] += 1
	elif i == "D":
		jog[3] += 1
print(jog)