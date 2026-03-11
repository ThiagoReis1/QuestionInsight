x = int(input())
a = x//1000
b = x%1000
prop = ((a - b)**2)
if(x == prop):
	print(prop," atende a propriedade")
else:
	print(prop)