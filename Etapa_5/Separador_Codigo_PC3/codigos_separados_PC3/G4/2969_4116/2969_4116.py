q = int(input("Digite a quantidade de jogos: "))
j1 = float(input("Digite o preco do jogo: "))

if  q == 1:
   mensagem = j1
else:
   j2 = float(input("Digite o preco do segundo jogo: "))
   mensagem = ((j2 / 100) * 75) + j1
	
print(round(mensagem, 2))	