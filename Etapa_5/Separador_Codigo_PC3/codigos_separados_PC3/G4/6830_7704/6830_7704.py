from numpy import*

p= input().upper()

i=0
s=0

while i<len(p):
	if p[i] == "H":
		s+=3.85
	if p[i]== "L":
		s+=2.95
	if p[i] == "E":
		s+=7.90
	i+=1
	
print(round(s, 2))
		