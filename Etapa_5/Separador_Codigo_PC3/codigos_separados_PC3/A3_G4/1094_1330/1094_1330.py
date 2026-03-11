X = int(input())
v = X%1000
z = X//1000
if(((v+z)**2)==X):
	y = ((v+z)**2)
	print (X,"atende a propriedade")
else:
	print ((v+z)**2)