from numpy import*
jogador_1= array(eval(input("vetor do jogador 1: ")))
jogador_2= array(eval(input("vetor do jogador 2: ")))
[1]= 40
[2]= 20
[3]= 10
[4]= 0
if (sum(jogador_1) > (sum(jogador_2))):
	print ("JOGADOR UM")
elif (sum(jogador_2) > (sum(jogador_1))):
	print("JOGADOR DOIS")
else:
	print("EMPATE")
	