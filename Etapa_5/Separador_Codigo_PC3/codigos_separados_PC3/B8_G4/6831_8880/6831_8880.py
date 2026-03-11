from numpy import*
p= input(" ").upper()
c=0
v=0

while c <len(p):
	if p[c]== "A":
		v+= 16.75
	elif p[c]== "L":
		v+=4.60
	elif p[c]== "P":
		v+= 2.85
	c+=1
	
print(round(v,2))