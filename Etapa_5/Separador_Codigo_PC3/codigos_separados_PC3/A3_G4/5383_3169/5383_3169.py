from numpy import*
x = input(":").upper()
i = 0
j = 0
a = 0

while i<x[i]:
	if (x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u'):
		j = j + 1
		a = j * 0.12
	else:
		j = j + 1
		a = j * 0.18
	i = i + 1
print(round(j, 2))