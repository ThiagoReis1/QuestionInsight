n=int(input())
a=n//10000
b=n%10000
x=((a+b)**2)
print(n)
if(n==x):
	print("atende")
else:
	print("nao atende")
