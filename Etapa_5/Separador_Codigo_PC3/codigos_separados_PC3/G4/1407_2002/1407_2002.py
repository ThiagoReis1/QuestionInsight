
hp0 = int(input("HP iniciais do personagem: "))
a = int(input("Valor da face: "))
b = int(input("Valor da face: "))
c = int(input("Valor da face: "))

# Lei que define o dano recebido
hplost = 10 * (a+b+c)

if hp0 - hplost > 0:
	print(hp0 - hplost)
	print("VIVO")
else:
	print(0)
	print("MORTO")