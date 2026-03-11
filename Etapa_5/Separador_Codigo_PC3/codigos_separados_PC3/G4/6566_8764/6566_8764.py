# faça seu código aqui!
q = int(input("Digite a qtd de pecas de roupas: "))

tf = 30.00

if(q < 10):
	t = 3.25
	valor = tf + t
elif (q == 10):
	t = 4.50
	valor = tf + t
else:
	t = 6.00
	valor = tf + t
print("total=", round(valor, 2))