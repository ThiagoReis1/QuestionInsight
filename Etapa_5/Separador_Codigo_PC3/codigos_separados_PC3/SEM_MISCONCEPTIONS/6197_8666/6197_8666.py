# questao quatro alternativa
	print(num)
	n = n + 1
print("fim")
altura = float(input("altura: "))
taxacrescimento = float(input("taxa de crescimento: "))
tj = 0.02
aj = 1.6
conta = 0
while (altura < aj):
	altura += taxacrescimento
	aj += tj
	conta +=1
print(conta)

