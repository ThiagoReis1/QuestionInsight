valor = int(input("Digite o numero"))

a = (valor // 100.0)
b = (valor % 100.0)
c = (a**2+b**2)
if (c == valor):
   print("X atende a propriedade")
else:
	print(c)