x = int(input("digite o valor de x: "))
q = (x//37)
r = (x%37)
if r == 0:
	mensagem1 = "sim"
	print(q)
	print(mensagem1)
else:
	mensagem2 = "nao"
	print(r)
	print(mensagem2)