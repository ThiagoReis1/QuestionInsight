x = input("Insira o nome do ataque: ")
y = int(input("Insira o valor do dado 1: "))
z = int(input("Insira o valor do dado 2: "))

if(x.lower() == 'grito'):
	dano = 6 + y + z
else:
	w = (y + z) ** 2
	dano = (w)

print(dano)