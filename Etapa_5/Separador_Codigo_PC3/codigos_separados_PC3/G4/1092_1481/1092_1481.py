#victor do vale moreira
#av.02
#14/07/2016

n = int(input("Digite um numero de tres digitos:"))
a1 = n // 100
a2 = (n // 10) % 10
a3 = n % 10
x = (a1 ** 3) + (a2 ** 3) + (a3 ** 3)
X = n
if (n == x):
	print(X,"atende a propriedade"  )
else:
	print(x)	