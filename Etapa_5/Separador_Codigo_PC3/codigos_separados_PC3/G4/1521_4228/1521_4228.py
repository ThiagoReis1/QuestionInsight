n = int(input("Capacidade de Containers: "))
x = int(input("Estoque inicial: "))
q = int(input("Quantidade de Containers: "))

while (n > x + q):
	n = n + q/7
	