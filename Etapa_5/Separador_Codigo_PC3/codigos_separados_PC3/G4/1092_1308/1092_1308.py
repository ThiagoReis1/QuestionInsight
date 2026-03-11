X=int(input("Digite o numero X:"))
a=X//100
b=(X%100)//10
c=(X%100)%10
s=a**3+b**3+c**3
if(s==X):
	print(X,"atende a propriedade")
else:
	print(s)