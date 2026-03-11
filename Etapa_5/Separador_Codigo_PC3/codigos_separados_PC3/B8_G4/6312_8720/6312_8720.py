s=input().upper()
i=0
b=0
e=0
c=0
while i<len(s):
	if s[i]=="B":
		b=b+1
	elif s[i]=="C":
		c=c+1
	elif s[i]=="E":
		e=e+1
	i=i+1
t=(e*9.85)+(c*7.90)+(b*3.75)
print(round(t,2), b, c, e)