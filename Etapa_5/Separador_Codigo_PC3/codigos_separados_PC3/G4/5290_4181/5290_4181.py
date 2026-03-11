v = int(input("valor: "))
c = 0
s=0

while (v != -1):
	c = c +1
	if(v == 5):
		s = s+1
	v = int(input("face"))

p = (s/c)*100
print(c)
print(round(p, 2))