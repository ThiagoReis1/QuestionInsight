v = input(": ").upper()
i = 0
t = 0
while i<len(v):
	if v[i]=="H":
		t += 5.40
	elif v[i]=="C":
		t +=8.95
	elif v[i]=="L":
		t +=4.50
	i+=1
print(round(t,2))