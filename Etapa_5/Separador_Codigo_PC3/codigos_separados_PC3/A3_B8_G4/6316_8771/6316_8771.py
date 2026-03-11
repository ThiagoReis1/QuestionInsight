from numpy import*
v=input().upper()
d=0
s=0
i=0
x=0
soma=0
while x!=len(v):
	if v[x]=='D':
		d+=1
	elif v[x]=='S':
		s+=1
	elif v[x]=='I':
		i+=1
	x+=1
total=d*2.25+s*4.0+i*6.9
print(round(total,2),d,s,i)
