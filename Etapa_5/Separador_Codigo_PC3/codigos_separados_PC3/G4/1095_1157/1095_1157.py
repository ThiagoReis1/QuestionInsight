X = int(input("numero"))
y = int(X%10000)
z = int(X // 10000)
if(X == ((y + z)**2)):
	print("X atende a propriedade")
else: 
	print((y + z)**2)
