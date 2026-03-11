v1 = float(input("valor da compra 1: "))
v2 = float(input("valor da compra 2: "))
v3 = float(input("valor da compra 3: "))
v4 = float(input("valor da compra 4: "))
limite = float(input("limite do cartao: "))

total = v1+v2+v3+v4
print(total)

if(total <= limite):
	mensagem = ("sim")
else:
	mensagem = ("nao")
print(mensagem)

