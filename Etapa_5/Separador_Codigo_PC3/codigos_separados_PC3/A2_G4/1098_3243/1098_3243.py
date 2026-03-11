n = int(input())

n1 = n // 1000
n2 = n % 1000

if((n1+n2)**4 == n):
	m = "atende"
	n = n
	
else:
	m = "nao atende"
	
print(n)
print(m)
