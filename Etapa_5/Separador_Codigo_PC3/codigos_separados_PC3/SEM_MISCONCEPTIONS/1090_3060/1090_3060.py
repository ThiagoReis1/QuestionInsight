l = float(input("Limite do Cartao: "))
c1 = float(input("Compra 1: "))
c2 = float(input("Compra 2: "))
c3 = float(input("Compra 3: "))
c4 = float(input("Compra 4: "))

t = c1 + c2 + c3 + c4
print(round(t, 2))

if (t <= l):
	print("Dentro do limite")
else:
	print("Estourou o limite")
é só reprovado, sem o 