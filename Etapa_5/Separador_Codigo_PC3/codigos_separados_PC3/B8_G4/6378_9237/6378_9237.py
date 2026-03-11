s = input()

c = 0
d = 0
v = 0
u = 0

for i in range(len(s)):
	if(s[i] == "C"):
		c = c + 1
	elif(s[i] == "D"):
		d = d + 1
	elif(s[i] == "V"):
		v = v + 1
	elif(s[i] == "U"):
		u = u + 1
v = [c , d , v , u]
print(v)