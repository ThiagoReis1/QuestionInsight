from numpy import*

jogador=input("insira o jogador A,B,C,D: ").upper().split(',')

gols=zeros(4,dtype=int)

for i in range(size(jogador)):
	if jogador[i]=="A":
		gols[0]=gols[0]+1
	elif jogador[i]=="B":
		gols[1]=gols[1]+1
	elif jogador[i]=="C":
		gols[2]=gols[2]+1
	elif jogador[i]=="D":
		gols[3]=gols[3]+1
		
print(gols)