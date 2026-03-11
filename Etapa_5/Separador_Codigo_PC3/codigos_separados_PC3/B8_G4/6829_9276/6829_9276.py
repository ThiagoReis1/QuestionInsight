d=input(" ").upper()
c=0
v=0

while c<len(d):
	if d[c]=="A":
		v+=19.90
	elif d[c]=="L":
		v+=3.50
	elif d[c]=="P":
	   v+=4.25
	c+=1
print(round(v,2))