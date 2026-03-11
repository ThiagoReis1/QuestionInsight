n=int(input("n:"))
a=n//1000
b=n%1000
x=(a-b)**2
if(n==x):
	print("atende")
else:
	print("nao atende")
print(n)