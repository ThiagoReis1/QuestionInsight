from numpy import*
x = input("produto: ")
i = 0
total = 0
while i < len(x):
	if x[i] == "H":
		total = total + 3.85
	if x[i] == "L":
		total = total + 2.95
	if x[i] == "E":
		total = total + 7.90
	i = i + 1
print(round(total, 2))