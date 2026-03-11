x = input(": ").upper()

s = 0
n = 0

while(x!='S'):
	if(x=='SIM'):
		s = s + 1
	elif(x=='NAO'):
		n = n + 1
	x = input(": ").upper()
	p = (s/(s+n))*100
print(s+n)
print(round(p, 2))