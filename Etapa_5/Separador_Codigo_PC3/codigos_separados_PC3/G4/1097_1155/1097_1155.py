x= int(input("Digite o numero"))
n1= x // 1000
r1= x % 1000
n2= r1 // 1
valor= (n1 - n2) ** 2
if(x == valor):
	print("X atende a propriedade")
else:
	print(valor)