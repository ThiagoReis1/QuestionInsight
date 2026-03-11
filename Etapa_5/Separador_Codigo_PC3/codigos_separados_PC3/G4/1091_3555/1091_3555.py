a=int(input())

n1=a//100
n2=(a-n1*100)


print(a)

if((n1+n2)*(n1+n2) == a):
	print("atende")
	
else:
	print("nao atende")

