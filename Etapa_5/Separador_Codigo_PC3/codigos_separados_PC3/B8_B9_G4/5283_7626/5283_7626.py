n= int(input(""))
p= 0
i= 0
c=0
while n != 0:
	if n < 0:
		p= p + 1
	elif n >= 0:
		i= i + 1
	c= c+1
	n= int(input(""))
t= p + i
pct= (i / t)* 100
print(t)
print(round(pct,2))