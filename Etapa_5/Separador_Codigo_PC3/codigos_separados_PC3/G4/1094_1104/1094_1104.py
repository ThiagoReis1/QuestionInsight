X=int(input("digite numero:"))
x1=X//10000
x2=X%10000//100
if((x1+x2)**2==X):
	msg="X atende a propriedade"
	print(msg)
else:
	S=(x1 + x2)**2
	print(S)