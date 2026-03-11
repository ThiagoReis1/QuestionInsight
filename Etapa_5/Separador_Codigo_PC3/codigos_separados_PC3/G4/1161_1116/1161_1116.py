z = float(input("Quantidade de zumbi: "))
h = float(input("Quantidade de habitantes: "))
x = float(input("Capacidade de transformação: "))
y = float(input("Capacidade de matar zumbis: "))
i = 1
while(h >= z):
	z = z * x
	z = z - y
	h = h - x
	i = i + 1
print(i)
	