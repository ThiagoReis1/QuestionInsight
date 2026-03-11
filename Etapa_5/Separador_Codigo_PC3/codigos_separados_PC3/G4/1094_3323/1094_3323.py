from math import*
n=int(input("mensagem"))
d1=n//1000
d2=n%1000


if n == (d1+d2)**2:
	print("atende")
else:
	print("nao atende")
	
print(n)

