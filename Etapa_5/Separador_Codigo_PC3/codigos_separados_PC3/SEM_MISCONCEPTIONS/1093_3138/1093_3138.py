n=int(input(""))

n1=n//1000
n2=(n//100) %10
n3=(n//10) %10
n4= n%10

doisnumeros=(n1*10)+n2

quatronumeros=(n3*10)+n4

quad1=(doisnumeros**2)
quad2=(quatronumeros**2)

if (quad1+quad2==n):
	print("atende")
	print(n)
	
else:
	print("nao atende")
	print(n)
