from numpy import *
cor=input("informe a cor:").split(',')
vetP=0
vetC=0
vetR=0
vetL=0
vetB=0
resposta=zeros(5, dtype=int)
for i in cor:
	if (i=="P"):
		vetP=vetP+1
	elif (i=="C"):
		vetC=vetC+1
	elif (i=="R"):
		vetR=vetR+1
	elif (i=="L"):
		vetL=vetL+1
	elif (i=="B"):
		vetB=vetB+1
		
for y in range(size(cor)):
	if (cor[y]=="P"):
		resposta=vetP
	elif (y=="C"):
		resposta=vetC
	elif (y=="R"):
		resposta=vetR
	elif (y=="L"):
		resposta=vetL
	elif (y=="B"):
		resposta=vetB
l=max(resposta)
print(l)
print(resposta)