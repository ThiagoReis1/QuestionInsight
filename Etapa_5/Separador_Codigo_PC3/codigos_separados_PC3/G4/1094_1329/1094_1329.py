a=int(input("Digite um numero:"))
b=a//1000
b1=a%1000
equacao=((b+b1)**2)
if(equacao==a):
	print(a,"atende a propriedade")
else:
	print(equacao)		
