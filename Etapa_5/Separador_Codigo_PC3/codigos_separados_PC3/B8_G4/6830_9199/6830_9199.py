s = input("Digite:")

h = 3.85
l = 2.95
e = 7.90
acum = 0
i = 0

while i < len(s):
	if s[i] == "H":
		total = h
		acum = acum + total
	elif s[i] == "L":
		total = l
		acum += total
	elif s[i] == "E":
		total = e
		acum += total
	i += 1	
	
print(round(acum,2))		