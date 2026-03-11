numero = int(input("digite o numero: "))

r1 = numero % 100
n1 = numero // 100

r2 = r1 % 10
n2 = r1 // 10

r3 = r2
n3 = r2

if(n1**3 + n2**3 + n3**3 == numero):
	mensagem = "atende"
else:
	mensagem = "nao atende"

print(numero)
print(mensagem)