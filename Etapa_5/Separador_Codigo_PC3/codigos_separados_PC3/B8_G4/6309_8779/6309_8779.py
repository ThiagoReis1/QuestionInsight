from numpy import*
p=input()
i=0
t=0
h=0
c=0
l=0
while i<len(p):
	if p[i]=='H':
		t+=5.40
		h+=1
	elif p[i]=='C':
		t+=8.95
		c+=1
	elif p[i]=='L':
		t+=4.50
		l+=1
	i+=1
print(round(t, 2), h, c, l)

