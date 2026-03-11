X = int(input("valor do numero"))
Y = (X//100)
Z = (X%100)
W = (Z+Y)
if(X == W**2):
	print("X atende a propriedade")
if(X != W**2): 
	print(W**2)	