et= 0
cdr=0
s= 0
while et!="X":
	cdr= cdr +1
	if et=="P":
		cdr = cdr +1
	elif et=="C":
		cdr == cdr +1
	elif et=="A":
		s= s+1
	et= input("entrada")
if et=="X":
	cdr = cdr -1
print(s)