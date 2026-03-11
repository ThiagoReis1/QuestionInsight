# Inserindo dados de entrada

opcao = input("A opcao desejada eh bolo (B) ou salgado (S): " ).upper()
qtde_comida = int(input("Qual a quantidade desejada?: "))
qtde_cappuccino = int(input("Qual a quantidade de cappuccino pedido: " ))

bolo = 5.00
salgado = 4.00
cappuccino = 7.50

if opcao == ("B"):
	valor_final = qtde_comida * bolo + qtde_cappuccino * cappuccino
	
else:
	valor_final = qtde_comida * salgado + qtde_cappuccino * cappuccino
	
print(round(valor_final, 2))