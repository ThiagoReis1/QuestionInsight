qi = int(input(""))
dm = int(input(""))
M = int(input(""))
R = int(input(""))

qi = qi + M - dm - R
i = 1

while (qi > 0):
	qi = qi + M - dm - R
	i = i + 1

print(i)