n= int(input())
a= n // 1000
b= n % 1000
c= (a-b)**2

if (n==c):
	print("atende")
	print(n)
else:
	print("nao atende")
	print(n)