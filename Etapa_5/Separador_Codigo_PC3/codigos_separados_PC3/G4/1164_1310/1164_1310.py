n=int(input("digite: "))
c=1
v=1
s=0
while c<=n:
	j=(4+v)
	b=(-1)**(1+c)
	s=((c**2)/j)*b + s
	v=(v+2)
	c=(c+1)
print(round(s,8))	
