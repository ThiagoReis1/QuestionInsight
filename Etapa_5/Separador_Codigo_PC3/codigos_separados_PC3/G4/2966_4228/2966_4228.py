D = input("Desconto para mulher: ")
var = i(input("Valor do ingresso: "))
x = input(input("Quantidade de ingressos: "))
k = 0.8
t1 = ((var * x) * k)
t2 = (var * x)
if (D == "s"):
	mensagem = t1
else:
	mensagem = t2
print(round(mensagem, 2))