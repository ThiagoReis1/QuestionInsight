# Monalisa Pereira 21600560
# 300616
# Av 02 - Ex 02

x = int(input("Insira o numero: "))
y = x // 1000
z = x % 1000

calculo = (y + z) ** 2

if (x == calculo):
	print("X atende a propriedade")
else:
	print(calculo)