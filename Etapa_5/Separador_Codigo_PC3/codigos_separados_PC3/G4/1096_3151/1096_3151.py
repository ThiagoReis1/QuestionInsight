n=int(input())
a=n//10000
b=(n//100)%100
c=n%100

if((a**3)+(b**3)+(c**3)==n):
	print("atende")
else:
	print("nao atende")
print(n)
	