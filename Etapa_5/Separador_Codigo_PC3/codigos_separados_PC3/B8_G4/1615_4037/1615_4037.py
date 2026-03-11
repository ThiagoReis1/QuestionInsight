from numpy import*
v1=array(eval(input("numeros do primeiro jogador: ")))
v2=array(eval(input("numeros do segundo jogador: ")))
i=0
p1=0
p2=0
while(i == 0):
	if(v1[i]==1):
		p1 += 40
	elif(v1[i]==2):
		p1 += 20
	elif(v1[i]==3):
		p1 += 10
	elif(v1[i]==4):
		p1 += 0
	if(v2[i]==1):
		p2 += 40
	elif(v2[i]==2):
		p2 += 20
	elif(v2[i]==3):
		p2 += 10
	elif(v2[i]==4):
		p2 += 0
	i += 1
if(p1 > p2):
	print("JOGADOR UM")
elif(p1 < p2):
	print("JOGADOR DOIS")
elif(p1 == p2):
	print("EMPATE")
		