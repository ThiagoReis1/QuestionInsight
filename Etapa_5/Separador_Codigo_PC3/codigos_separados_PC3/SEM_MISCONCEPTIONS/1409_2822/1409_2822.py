#Entrada de variaveis
ataque = input("Qual o ataque: ")
dado1 = int(input("Valor do dado 1: "))
dado2 = int(input("Valor do dado 2: "))
dado3 = int(input("Valor do dado 3: "))
dado4 = int(input("Valor do dado 4: "))
#Calculo para cada situação
if(ataque == "espada"):
	dano = (dado1 + 6) + (dado2 + 6) + (dado3 + 6) + (dado4 + 6)
else:
	dano =(dado1 + dado2 + dado3)*dado4
print(dano)