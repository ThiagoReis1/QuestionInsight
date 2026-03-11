n=int(input())
q=n//10000
w=n%10000
if(n==(q+w)**2):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")