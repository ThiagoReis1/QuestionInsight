x = int(input())

n1= x//1000
r1= x%1000

j= ((n1-r1)**2)

if(j==x):
	print("atende")
	print(x)
	
else:
	print("nao atende")
	print(x)