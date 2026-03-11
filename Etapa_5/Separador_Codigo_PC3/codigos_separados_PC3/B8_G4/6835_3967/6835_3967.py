p = input()

i = 0
t = 0

while i < len(p):
	if p[i] == "B":
		t = 3.75 + t
	elif p[i] == "C":
		t = 7.90 + t
	elif p[i] == "E":
		t = 9.85 + t
	i = i + 1
	
print(round(t,2))