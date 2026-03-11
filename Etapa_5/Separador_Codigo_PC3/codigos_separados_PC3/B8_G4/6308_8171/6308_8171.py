s=input("").upper()
total=0
i=0
a=0
l=0
p=0

while i<len(s):
	if s[i]=="A":
		total+=16.75
		a+=1
	elif s[i]=="L":
		total+=4.6
		l+=1
	elif s[i]=="P":
		total+=2.85
		p+=1
	i+=1
print(round(total,2),a,l,p)