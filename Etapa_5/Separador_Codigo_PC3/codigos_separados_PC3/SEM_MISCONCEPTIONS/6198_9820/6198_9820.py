altura_luna = 1.65
taxa_luna = 0.02

a1 = float(input(''))
t1 = float(input(''))

c = 0

while (a1 < altura_luna):
	altura_luna += taxa_luna
	a1 += t1
	c += 1
	
print (c)