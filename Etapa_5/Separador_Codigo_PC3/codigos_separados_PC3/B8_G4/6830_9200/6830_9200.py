p = input("digite: ")
i = 0
t = 0

while(i < len(p)):
	if(p[i] == "H"):
		h = 3.85
		t = t + h 
	elif(p[i] == "L"):
		l = 2.95
		t = t + l
	elif(p[i] == "E"):
		e = 7.90
		t = t + e
	i = i + 1

print(round(t,2))