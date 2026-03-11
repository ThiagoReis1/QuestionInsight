n=int(input())
n1=n//10000
n2=(n%10000)//100
n3=n%100
calculo=(n1**3)+(n2**3)+(n3**3)
if(calculo==n):
	print("atende")
	print(calculo)
else:
	print("nao atende")
	print(n)
	