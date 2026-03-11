nome = input("Digite a cabeça que Demogorgon atacará: ")
d1 = int(input("Dado 1: "))
d2 = int(input("Dado 2: "))
d3 = int(input("Dado 3: "))

if(nome == "Aameul"):
	dano = 8 + d1+d2+d3
else:
	dano = (d1+d2+d3)*2

print(dano)