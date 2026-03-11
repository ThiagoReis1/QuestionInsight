s= input('alimentos: ').upper()
x=0
i=0
c1=0
c2=0
c3=0
while(i<len(s)):
	if(s[i]=='H'):
		x=x+3.85
		c1=c1+1
	elif(s[i]=='L'):
		x=x+2.95
		c2=c2+1
	elif(s[i]=='E'):
		x=x+7.90
		c3=c3+1
	i=i+1
print(round(x,2),c1,c2,c3)