#-------------------------------------------
# Aluno: Ivan Lucas de Oliveira Pacheco
# Data: 07/12/2022
# Objetivo: Definir o preço do prato de um cliente em um café onde não é possivel pedir simultaneamente fatias de bolos e salgados
#-------------------------------------------

# Definição dos preços dos produtos
fatia_bolo = 5
fatia_salgado = 4
cappuccino = 7.5
conta = 0

# Leitura se a fatia é de bolo ou salgado
fatia = input("Digite B para fatia de bolo ou S para fatia de salgado: ")

fatia = fatia.upper()

if fatia == "B":
	qtd_fatia = int(input("Qual a quantidade de fatias? "))
	conta = qtd_fatia * fatia_bolo
else:
	qtd_fatia = int(input("Qual a quantidade de fatias? "))
	conta = qtd_fatia * fatia_salgado

qtd_cappu = int(input("Digite a quantidade de cappuccinos: "))

conta = conta + (cappuccino * qtd_cappu)

print(round(conta,2))