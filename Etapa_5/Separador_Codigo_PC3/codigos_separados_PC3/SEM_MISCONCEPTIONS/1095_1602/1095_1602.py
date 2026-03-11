X=float(input("qual o valor de X ?"))
restodeX2 = X // 10000 
restodeX1 = X % 10000
if(X==(restodeX1+restodeX2)**2):
	mensagen="X atende a propriedade"
	print(mensagen)
else:
	quad=int((restodeX1+restodeX2)**2)
	print(quad)