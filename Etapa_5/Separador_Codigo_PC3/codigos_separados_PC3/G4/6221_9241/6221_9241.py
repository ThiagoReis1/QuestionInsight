x= int(input("Digite o valor de x: "))
y= int(input("Digite o valor de y: "))

contas = x
soma= 0

while contas <= y:
	if contas % 7 == 0:
		soma = soma + contas
	contas= contas + 1
print(soma)