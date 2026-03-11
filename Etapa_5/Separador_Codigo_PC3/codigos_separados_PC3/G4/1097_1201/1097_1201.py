x=int(input())
x2=x//1000
x3=x%1000
if (x==(x2-x3)**2):
	print(x)
	print("atende a propriedade")
else:
	print((x2-x3)**2)
