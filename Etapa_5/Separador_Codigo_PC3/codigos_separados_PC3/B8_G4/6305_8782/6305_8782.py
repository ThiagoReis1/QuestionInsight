s= input("").upper()
i=0
sm=0
c=0
d=0
p=0
h =3.85
l= 2.95
e=7.90
while i < len (s):
	if s[i]=="H":
		sm = sm + h 
		c=c+1
	elif s[i] == "L":
		sm =sm+l
		d=d+1
	elif s[i] == "E":
		sm=sm+e
		p=p+1
	i+=1
print(round(sm,2))
print(c)
print(d)
print(p)
p

