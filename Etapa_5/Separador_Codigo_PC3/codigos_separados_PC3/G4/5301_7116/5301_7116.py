ra = int(input(": "))
c = 0

while(ra >= 40):
	ra = ra - (ra * 2/100)
	c = c + 1
print(c)