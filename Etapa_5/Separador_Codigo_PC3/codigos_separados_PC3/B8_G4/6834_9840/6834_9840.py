from numpy import*
s=input("manda:").upper()
tam=len(s)
i=0
c=0
while i<tam:
	if s[i]=="C":
		c=c+10.50
	elif s[i]=="E":
		c=c+8.75
	elif s[i]=="P":
		c=c+17.90
	i+=1
print(round(c,2))
		
