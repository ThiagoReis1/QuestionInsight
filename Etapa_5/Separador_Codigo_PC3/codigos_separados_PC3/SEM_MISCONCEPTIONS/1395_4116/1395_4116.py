V = float(input("Valor de vendas: "))
v2 = (1000.0 / 100) * 5
if V <= 1000.0:
   mensagem = (V / 100) * 5
else:
	mensagem = (((V - 1000.0) / 100) * 10 ) + v2
print(round(mensagem, 2))