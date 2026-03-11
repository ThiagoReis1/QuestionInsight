from numpy import*
v=input().upper()

i=0
s=0
while i<len(v):
	if v[i]=="H":
		s=s+5.40
	elif v[i]=="C":
		s=s+8.95
	elif v[i]=="L":
		s=s+4.50
	i+=1
print(round(s,2))