n = int(float(input(":")))

n1 = n//100
rn1 = n % 100
d = (n1**2) + (rn1**2)

if(d == n):
	print("atende")
	print(d)
else:
	print("nao atende")
	print(n)
	

