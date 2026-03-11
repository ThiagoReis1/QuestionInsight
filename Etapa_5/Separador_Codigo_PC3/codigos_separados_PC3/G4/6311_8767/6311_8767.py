n = input("").upper()
c = 0
e = 0
p = 0
acm = 0
i = 0
while len(n) > i:
	if n[i] == "C":
		acm = acm +10.50 
		c = c + 1
	if n[i] == "E":
		acm = acm +8.75
		e = e + 1
	if n[i] == "P":
		acm =acm+ 17.90 
		p = p + 1 
	i = i + 1 
print(round(acm,2),c,e,p)