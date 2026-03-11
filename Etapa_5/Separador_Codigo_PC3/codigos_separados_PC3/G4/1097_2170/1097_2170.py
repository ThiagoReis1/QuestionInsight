n=int(input(":"))
n1= n// 1000
n2= n% 1000

r=( n1 - n2)**2

if(r == n):
	print("atende")
	print(r)
else:
	print("nao atende")
	print(n)