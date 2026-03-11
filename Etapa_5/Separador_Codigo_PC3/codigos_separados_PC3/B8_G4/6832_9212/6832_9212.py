from numpy import*

pr = input("digite a string:")
i = 0
j = 0

while i < len(pr):
	if pr[i] == "H":
		j += 5.40
	elif pr[i] == "C":
		j += 8.95
	elif pr[i] == "L":
		j += 4.50
	i += 1
print(round(j,2))