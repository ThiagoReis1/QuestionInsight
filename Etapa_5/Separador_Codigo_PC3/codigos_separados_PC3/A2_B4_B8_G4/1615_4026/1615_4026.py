from numpy import*
j1=array(eval(input("Aneis acertados pelo primeiro jogador:")))
j2=array(eval(input("Aneis acertados pelo segundo jogador:")))
m=size(j1)
p1=0
p2=0
i=0
while	(i<m):
	#Vitoria Jogador 1
	if	(j1[i]==1)	and	(j2[i]==2):
		p1=p1+1
	elif	(j1[i]==1)	and	(j2[i]==3):
		p1=p1+1
	elif	(j1[i]==1)	and	(j2[i]==4):
		p1=p1+1
	elif	(j1[i]==2)	and	(j2[i]==3):
		p1=p1+1
	elif	(j1[i]==3)	and	(j2[i]==4):
		p1=p1+1
	#Vitoria Jogador 2
	elif	(j2[i]==1)	and	(j1[i]==2):
		p2=p2+1
	elif	(j2[i]==1) and	(j1[i]==3):
		p2=p2+1
	elif	(j2[i]==1) and (j1[i]==4):
		p2=p2+1
	elif	(j2[i]==2)	and	(j1[i]==3):
		p2=p2+1
	elif	(j2[i]==2) and	(j1[i]==4):
		p2=p2+1
	elif	(j2[i]==3)	and	(j1[i]==4):
		p2=p2+1
	#EMPATE
	elif	(j1[i]==j2[i]):
		p1=p1
		p2=p2
	i=i+1
if	(p1>p2):
	print("JOGADOR UM")
if	(p2>p1):
	print("JOGADOR DOIS")
if	(p1==p2):
	print("EMPATE")