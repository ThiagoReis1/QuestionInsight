X = int(input("valor do numero" ))
a = X // 100
n = X % 100 // 1
if( X == (a + n)**2):
	print("X atende a propriedade")
else:
	print((a + n)**2)