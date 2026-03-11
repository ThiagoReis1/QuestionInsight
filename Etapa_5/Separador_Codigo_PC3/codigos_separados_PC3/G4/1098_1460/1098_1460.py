# Luiz Matheus Abecassis Ferreira Brito
# Exercicio 2

x = int(input("informe o valor de X: "))
x1 = x // 1000
x2 = x % 1000
x3 = (x1 - x2) ** 4

if (x == x3):
	print(x,"atende a propriedade")		
	
else:
	print(x3)