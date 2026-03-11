n=int(input())
x=n//1000
y=n%1000
a=(x-y)**2
if(a==n):
	print("atende")
	print(a)
else:
	print("nao atende")
	print(n)