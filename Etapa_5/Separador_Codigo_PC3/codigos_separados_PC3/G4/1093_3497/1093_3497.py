x=int(input())
ab=x//100
ra=x%100
r = (ab**2)+(ra**2)

if(r==x):
	print("atende")
	print(x)
else:
	print("nao atende")
	print(x)


