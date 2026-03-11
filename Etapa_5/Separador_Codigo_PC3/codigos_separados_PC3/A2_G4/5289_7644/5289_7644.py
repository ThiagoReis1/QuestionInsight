d = int(input("lado do dado: "))
l = 0
s = 0
while(d != -1):
	l = l + 1
	if(d == 6):
		s = s+1
	else:
		s = s
	d = int(input("lado do dado: "))
p = s/l* 100
print(l)
print(round(p, 2))
