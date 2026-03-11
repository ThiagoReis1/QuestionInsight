n = float(input())

n1 = n//100
n2 = n%100

c = (n1 + n2)**2

if (c == n):
	print (int(n))
	print ("atende")
else:
	print (int(n))
	print ("nao atende")