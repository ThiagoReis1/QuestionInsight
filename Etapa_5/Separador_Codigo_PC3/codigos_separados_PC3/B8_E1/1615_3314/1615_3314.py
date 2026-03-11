from numpy import *
j1 = array(eval(input("Fale a pontuacao do jogador um: ")))
j2 = array(eval(input("Fale a pontuacao do jogador dois: ")))
i = 0 
cont1 = 0
cont2 = 0
while (i<size(j1)):
	if (j1[i] != j2[i]):
		if (j1[i]==4 and j2[i]==1) or (j1[i]==4 and j2[i]==2) or (j1[i]==4 and j2[i]==3) or (j1[i]==3 and j2[i]==1) or (j1[i]==3 and j2[i]==2) or (j1[i]==2 and j2[i]==1):
			cont1 = cont1 + 1
		elif (j2[i]==4 and j1[i]==1) or (j2[i]==4 and j1[i]==2) or (j2[i]==4 and j1[i]==3) or (j2[i]==3 and j1[i]==1) or (j2[i]==3 and j1[i]==2) or (j2[i]==2 and j1[i]==1):
			cont2 = cont2 + 1
	i = i + 1

if (cont1 > cont2):
	print("JOGADOR UM")
elif (cont2 > cont1):
	print("JOGADOR DOIS")
else:
	print("EMPATE")