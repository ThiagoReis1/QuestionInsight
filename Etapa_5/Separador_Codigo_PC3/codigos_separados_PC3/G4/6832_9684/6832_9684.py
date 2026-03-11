v = input("")
s = 0
i = 0
t = len(v) -1
while i <= t:
	if v[i] == "H": 
		s += 5.40
	if v[i] == "C":
		s += 8.95
	if v[i] == "L":
		s += 4.50
	i += 1
print(round(s, 2))






