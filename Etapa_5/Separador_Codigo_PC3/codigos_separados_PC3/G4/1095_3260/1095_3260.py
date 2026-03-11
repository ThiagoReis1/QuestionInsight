n = int(input("numero= "))

n1 = n//10000000
s1 = n%10000000

n2 = s1//1000000
s2 = s1%1000000

n3 = s2//100000
s3 = s2%100000

n4 = s3//10000
s4 = s3%10000

c = ( s4 + (n4*1 + n3*10 + n2*100 + n1*1000))**2

if c == n:
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")