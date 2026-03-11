# Leitura de variáveis
nome = input("Insira o nome do ataque realizado pela Banshee: ")
D1 = int(input("Insira o valor sorteado do dado 1: "))
D2 = int(input("Insira o valor sorteado do dado 2: "))

if(nome == "grito"):
	dano = 6 + (D1 + D2)
if(nome == "toque"):
	dano = (D1 + D2) ** 2
	
print(dano)

