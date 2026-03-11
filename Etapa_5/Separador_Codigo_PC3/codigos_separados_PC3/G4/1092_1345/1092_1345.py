numero=int(input("Insira um numero inteiro:"))

y=numero//100
z=numero%100
x=z//10
k=z%10

if(numero==y**3+x**3+k**3):
	print(numero,"atende a propriedade")
else:
	print(y**3+x**3+k**3)