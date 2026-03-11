#X eh a quantidade de jogos
X=int(input("digite 1 se levar apenas um jogo ou 2 se levar o segundo jogo: "))
#Y eh o valor do primeiro jogo
valorY=float(input("digite o valor do primeiro jogo: "))
if(X==1):
	valortotal=valorY
	print(round(valortotal,2))
else:
	#T eh o valor do segundo jogo
	valorZ=float(input("digite o valordo segundo jogo: "))
	#valortotal eh o valor total da compra quando for 2 jogos
	#D eh o desconto de 25% no valor do segundo jogo
	D=(0,25*valorZ)
	valortotal=valorY+(valorZ-D)
	print(round(valortotal,2))
