c= input("").upper()
t=0
i=0
ic=0
ie=0
ip=0
while i<len(c):
	if c[i]=="C":
		t+=10.50
		ic+=1
	if c[i]=="E":
		t+=8.75
		ie+=1
	if c[i]=="P":
		t+=17.90
		ip+=1
	i+=1
print(round(t, 2), ic, ie, ip)
	

	
	
	