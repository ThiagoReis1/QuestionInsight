from numpy import*
j1 = array(eval(input("jogada 1: ")))
j2 = array(eval(input("jogada 2: ")))
i = 0
j = 0
p1 = 0
p2 = 0 
#soma dos vetores dá a pontuação
#while(i<size(j1)):
	#if(j1[i]==1):
		#p1 = p1 + 40
while(i<size(j1)):
	if(j1[i]==1):
		p1 = p1 + 40
	elif(j1[i]==2):
		p1 = p1 + 20
	elif(j1[i]==3):
		p1 = p1 + 10
	elif(j1[1]>=4):
		p1 = p1 + 0
	i = i + 1	
while(j<size(j2)):
	if(j2[j]==1):
		p2 = p2+ 40
	elif(j2[j]==2):
		p2 = p2 + 20
	elif(j2[j]==3):
		p2 = p2 + 10
	elif(j2[j]==4):
		p2 = p2 + 0
	j = j + 1
if(p1>p2 or p2<p1):
	print("JOGADOR UM")
elif(p2>p1 or p1<p2):
	print("JOGADOR DOIS")
elif(p1==p2):
	print("EMPATE")

	