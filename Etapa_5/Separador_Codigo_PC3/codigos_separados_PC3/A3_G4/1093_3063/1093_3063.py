n=int(input("digite o numero"))
n1 = n//1000
n2 = n//100%10
n3 = n//10%10
n4 = n%10

n12 = n//100
n34 = n%100

ct1 = (n12)**2 + (n34)**2

if (ct1 == n):
	print("atende")
	print(n)
else:
	print("nao atende")
	print(n)
