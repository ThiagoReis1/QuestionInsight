from math import *
n= int(input())

a=(n//1000)
b=(n%1000)

x=(a-b)**2
if(x==n):
	msg="atende"
	print(msg)
	print(n)
else:
	msg="nao atende"
	print(msg)
	print(n)
	