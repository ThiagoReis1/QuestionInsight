c1 = float(input("valor da compra"))
c2 = float(input("valor da compra"))
c3 = float(input("valor da compra"))
li = float(input("valor do limite"))

if (c1 + c2 + c3 <= li):
   mensagem = "Nao ultrapassou"
else:
	mensagem = "Ultrapassou"
print(c1 + c2 + c3)
print(mensagem)