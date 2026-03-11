n = input("n :").upper()
a = 16.75
l = 4.60
p = 2.85
i = 0
c1 = 0
c2 = 0
c3 =0
while i<len(n):
	if n[i] == 'A':
		c1 = c1+1
	elif n[i] == 'L':
		c2=c2+1
	elif n[i] == 'P':
		c3 =c3+1
	i = i+1
v = (c1*a) + (c2*l) + (c3*p)
print(round(v, 2),c1,c2,c3)
	