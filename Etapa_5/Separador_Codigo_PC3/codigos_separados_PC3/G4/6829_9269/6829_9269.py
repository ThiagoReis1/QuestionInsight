from numpy import*
s = input(" ")
i = 0
t1,t2,t3 = 0,0,0
aco = 0
lat = 0
pad = 0

while (i < len(s)):
	if(s[i] == "A"):
		aco = aco + 19.90
		t1 = t1 + 1
	if(s[i] == "L"):
		lat = lat + 3.50
		t2 = t2 + 1
	if (s[i] == "P"):
		pad = pad + 4.25
		t3 = t3 + 1
	i += 1
print(round(aco + lat + pad, 2))
		
		
