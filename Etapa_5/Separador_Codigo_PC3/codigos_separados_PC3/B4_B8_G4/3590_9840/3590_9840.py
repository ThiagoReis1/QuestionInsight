from numpy import*
s=eval(input("manda:"))
tam=size(s)
i=0
c=0
while i<tam:
	if s[i]==1:
		c=c+10
	elif s[i]==2:
		c=c+5
	elif s[i]==3:
		c=c+0
	elif s[i]==4:
		c=c+5
	elif s[i]==5:
		c=c+20
	elif s[i]==6:
		c=c+10
	i+=1
print(c)