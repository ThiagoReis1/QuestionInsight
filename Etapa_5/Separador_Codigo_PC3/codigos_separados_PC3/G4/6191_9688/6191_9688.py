j = input("Cara ou coroa:").upper()
c = 0  
p = 0
while j != 'S':
	if j == 'CARA':
		c = c + 1
	else:
		p == 'COROA'
		p = p + 1

print(round(c/p)*100,2)
print(p)