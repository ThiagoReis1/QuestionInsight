#Karen Hanna Schoaba - 21600523
#Avaliacao 02 - Ex02
#30/06/2016

x=int(input("numero"))
x1=x//100
x2=x%100
y=x1**2+x2**2

if y==x:
	print(x,"atende a propriedade")
else:
	print(y)	