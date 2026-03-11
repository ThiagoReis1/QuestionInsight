s=input('senha: ').upper()

i=0
g=0
h=0
while i<len(s):
	if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
		g=g+1
	else:
		h=h+1
	i=i+1
c=g*3.15+h*4.17
print(round(c,2))
