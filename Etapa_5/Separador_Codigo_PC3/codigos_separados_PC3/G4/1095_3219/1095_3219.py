n= int(input())

a=(n//10000)
#print(a)
b= n % 10000
#print(b)
c= (a+b)**2
print(n)

if (c == n):
	print("atende")
	
else:
	print("nao atende")