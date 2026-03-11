n = input().upper()

i = 0
v = 0
c = 0 

while(i < len(n)):
	if (n[i] == "A") or (n[i] == "E") or (n[i] == "I") or (n[i] =="O") or (n[i] == "U"):
		v = v + 1
	else:
		c = c + 1
	i = i + 1 
t = (v*45.15)+(50.17*c)
print(round(t,2))