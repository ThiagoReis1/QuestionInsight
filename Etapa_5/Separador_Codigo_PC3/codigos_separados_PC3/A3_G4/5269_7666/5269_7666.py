a = 0
c = 0
d = 0


b = int(input())

while(b != 0):
	d = d + 1
	if(b%3 == 0):
		c = c + 1
	
	b = int(input())

print(d)
print(round(100*c/d,2))