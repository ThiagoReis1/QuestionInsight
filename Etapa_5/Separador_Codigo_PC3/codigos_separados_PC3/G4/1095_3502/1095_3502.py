from math import*
num= int(input())
a=(num//10000)
b=(num%10000)
x= (a+b)**2
if (x==num):
	mensagem= "atende"
	print(num)
	print(mensagem)
else:
	mensagem= "nao atende"
	print(num)
	print(mensagem)