n = int(input("quantidade: "))

if (n <10):
	p = 0.9*n
else:
	p = 0.75*n
print(round(p, 2))