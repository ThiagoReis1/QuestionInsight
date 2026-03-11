n = int(input("numero"))
n1 = n//10000
n2 = n % 10000
calculo = (n1 + n2)**2
if(n==calculo):
	m ="atende"
else:
	m ="nao atende"
	
print(n)
print(m)