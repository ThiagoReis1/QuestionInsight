X = int(input("informe um numero inteiro de quatro digitos: "))

p1 = X // 100
p2 = (X % 100)
s = ((p1**2) + (p2**2))

if (X == s):
	print(X,"atende a propriedade")
	
else:
	
	print(s)


