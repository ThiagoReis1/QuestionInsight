#Marcos Felipe Melo de Lima

x =int(input("Defina o valor de x com 6 numeros: "))
x1 = x // 100000 				#primeiro numero
x1_1 = x % 100000				#restante do numero
x2 = x1_1 // 10000 
x2_2 = x1_1 % 10000
x3 = x2_2 // 1000
x3_3 = x2_2 % 1000			#3 ultimos numeros
x4 = x // 1000					#3 primeiros numeros
valor = (x4 - x3_3) ** 2 

if (x == valor):
	print(x, "atende a propriedade")
else:
	print(valor)