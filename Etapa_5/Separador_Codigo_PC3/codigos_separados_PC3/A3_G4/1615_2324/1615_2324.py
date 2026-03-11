from numpy import*
vet1=array(eval((input())))
vet2=array(eval((input())))
X=0
y=0
if vet1[0]==3 and vet1[1]==1 and vet1[2]==1 and vet1[3]==4:
	x=x+1
	if vet2[0]==2 and vet2[1]==4 and vet2[2]==1 and vet2[3]==2:
		y=y+1
		if(x>y):
			print("JOGADOR UM")
else:
	print("JOGADOR DOIS")