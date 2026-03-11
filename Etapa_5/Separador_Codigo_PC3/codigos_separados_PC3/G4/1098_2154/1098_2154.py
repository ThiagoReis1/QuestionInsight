a = int(input())

d1 = a//1000
d2 = a%1000

b = (d1-d2)**4

if(b==a):
	print(a)
	print("atende")
else:
	print(a)
	print("nao atende")